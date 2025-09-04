
# اول send اجرا شود
commit 2:
docker exec -it -e PYTHONPATH=/app python_test python app/send.py
docker exec -it -e PYTHONPATH=/app python_test python app/receive.py

commit 3:
docker exec -it -e PYTHONPATH=/app python_test python app/test_producer.py
docker exec -it -e PYTHONPATH=/app python_test python app/worker.py

commit 4:
docker exec -it -e PYTHONPATH=/app python_test python app/receive_logs.py >logs_fromRabbit.log               and
docker exec -it -e PYTHONPATH=/app python_test python app/receive_logs.py
docker exec -it -e PYTHONPATH=/app python_test python app/emit_log.py

commit 5:
# اجرای هم زمان این دو
docker exec -it -e PYTHONPATH=/app python_test python app/reveive_direct_logs.py info warning error
docker exec -it -e PYTHONPATH=/app python_test python app/receive_direct_logs.py error >logs_fromRabbit_direct.log
docker exec -it -e PYTHONPATH=/app python_test python app/emit_direct_logs.py  error "error message"   # show in console
docker exec -it -e PYTHONPATH=/app python_test python app/emit_direct_logs.py  info "info error"       # show in file and console

commit 6 :
docker exec -it -e PYTHONPATH=/app python_test python app/receive_logs_topic.py "*.*.Rabbit" "lazy.#"
docker exec -it -e PYTHONPATH=/app python_test python app/receive_logs_topic.py "*.orange.*"
docker exec -it -e PYTHONPATH=/app python_test python app/emit_log_topic.py "quicke.orange.fox" 'a orange dog'

commit 7 :
docker exec -it -e PYTHONPATH=/app python_test python app/rpc_server.py
docker exec -it -e PYTHONPATH=/app python_test python app/rpc_client.py

# نمایش لیست صف ها , تبادل کننده ها
docker exec -it rabbitmq_test rabbitmqctl list_queues
docker exec -it rabbitmq_test rabbitmqctl list_queues messages_ready messages_unacknowledged
docker exec -it rabbitmq_test rabbitmqctl list_exchanges
docker exec -it rabbitmq_test rabbitmqctl list_bindings

# Different modes of running the application
# for testing
docker compose --env-file .env.test up --build          for testing with build
docker compose --env-file .env.test up                  for testing without build
docker exec -it python_test python main.py              run main in test container

# for debugging mode
docker compose --env-file .env.dev up --build           for development and debug with build
docker compose --env-file .env.dev up                   for run without build
docker exec -it python_debug python main.py

# for production mode
docker compose --env-file .env.prod up --build          for production with build
docker compose --env-file .env.prod up                  for production without build
docker exec -it python_production python main.py

# common commands
# build and run
docker-compose build python-rabbit
docker-compose up -d
docker compose ps
docker compose logs -f python-rabbit
docker exec -it python_test bash
docker compose down -v



# run test
docker exec -it python_test pytest .       #run all tests without show print in console
docker exec -it python_test pytest -s        #run all tes with show print in console
docker exec -it python_test pytest -v        #show more details
docker exec -it python_test pytest -v -k "test_singleton_connection"   #run specific test
docker exec -it python_test pytest -v -k "test_singleton_connection" --maxfail=1 --disable-warnings -q   #stop on first fail and disable warnings
docker exec -it python_test pytest -vvv        # show status of test for each file     PASSED or FAILED
