start:
	flask --app example --debug run --port 8000

tst_app:
	flask --app dev/app --debug run --port 8000

dbg_app:
	flask --app dev/app run --port 8000 --debug --no-debugger --no-reload