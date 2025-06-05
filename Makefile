.PHONY: init
init:
	rye sync

.PHONY: run
run: stop
	rye run python bot.py

.PHONY: run-back
run-back: stop
	rye run python bot.py &

.PHONY: stop
stop:
	pkill -f "bot.py" || true