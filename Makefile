.PHONY: init
init:
	rye sync

.PHONY: run
run:
	rye run python bot.py

.PHONY: run-back
run-back:
	nohup rye run python bot.py &

.PHONY: stop
stop:
	pkill -f "bot.py" || true