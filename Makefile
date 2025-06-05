init:
	rye sync

run:
	rye run python bot.py

run-back:
	rye run python bot.py &

stop:
	kill $(shell pgrep -f bot.py)