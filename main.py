import sys
import argparse
import asyncio
import errno
import logging
from aiopath import Path
import aioshutil

logger = logging.getLogger(__name__)

async def check_paths(src_path, dst_path):
    if await src_path.absolute() == await dst_path.absolute():
        raise ValueError(f"{src_path} and {dst_path} are the same directory")
    if dst_path.is_relative_to(src_path):
        raise ValueError(f"{dst_path} cannot be inside {src_path.absolute()}")

async def validate_source(src_path):
    if not await src_path.exists():
        raise FileNotFoundError(errno.ENOENT, f"{src_path} does not exist")
    if not await src_path.is_dir():
        raise NotADirectoryError(errno.ENOTDIR, f"{src_path} is not a directory")

async def validate_destination(dst_path):
    if await dst_path.exists() and not await dst_path.is_dir():
        raise NotADirectoryError(errno.ENOTDIR, f"{dst_path} is not a directory")
    if await dst_path.exists():
        async for _ in dst_path.iterdir():
            raise OSError(errno.ENOTEMPTY, f"{dst_path} is not empty")

async def copy_file(src: Path, dst: Path):
    file_name = src.name
    file_ext = src.suffix[1:].lower() or "no_extension"
    dir_name = src.parent
    
    dst_dir = dst / file_ext / Path(*dir_name.parts[1:]) 
    
    if await dst_dir.exists():
        if await dst_dir.is_file():
            logger.error(f"Target '{dst_dir}' is a file, not a directory.")
            return
    else:
        await dst_dir.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Created directory: {await dst_dir.absolute()}")

    dst_file = dst_dir / file_name

    logger.info(f"Copying: {await src.absolute()} -> {await dst_file.absolute()}")
    
    try:
        await aioshutil.copy(src, dst_file)
    except Exception as e:
        logger.error(f"Failed to copy {src}: {e}")

async def read_folder(srcdir: Path, dstdir: Path):
    async for path in srcdir.iterdir():
        if await path.is_dir():
            await read_folder(path, dstdir)
        else:
            await copy_file(path, dstdir)

async def main():
    parser = argparse.ArgumentParser(description="Recursive file copier.")
    parser.add_argument("srcdir", type=str, help="source directory")
    parser.add_argument("-d", "--dstdir", type=str, default="dist", help="destination directory")
    parser.add_argument("-v", "--verbose", action="store_true", help="show progress logs")

    args = parser.parse_args()

    if args.verbose:
        log_level = logging.INFO
    else:
        log_level = logging.CRITICAL

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    src_path = Path(args.srcdir)
    dst_path = Path(args.dstdir)

    try:
        await check_paths(src_path, dst_path)
        await validate_source(src_path)
        await validate_destination(dst_path)
        
        await read_folder(src_path, dst_path)

    except Exception as e:
        logger.critical(f"CRITICAL ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.critical("Process interrupted by user")
        sys.exit(130)