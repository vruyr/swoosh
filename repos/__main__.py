import sys, asyncio
from . import cli


def _smain(args):
	if sys.platform == "win32":
		loop = asyncio.ProactorEventLoop()
		asyncio.set_event_loop(loop)
	else:
		loop = asyncio.get_event_loop()
	loop.run_until_complete(cli.main(args, loop=loop))


if __name__ == "__main__":
	try:
		sys.exit(_smain(sys.argv[1:]))
	except KeyboardInterrupt:
		print(file=sys.stderr)
