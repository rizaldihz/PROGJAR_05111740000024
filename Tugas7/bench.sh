for i in 1 5 10
do
	ab -n 10 -c $i http://127.0.0.1:10001/
done

for i in 1 10 30 50
do
        ab -n 50 -c $i http://127.0.0.1:10001/
done
