echo 'a1'
ab -n 1000 -c 1 -r -k -s 99999 http://127.0.0.1:45000/
echo 'a10'
ab -n 1000 -c 10 -r -k -s 99999 http://127.0.0.1:45000/
echo 'a50'
ab -n 1000 -c 50 -r -k -s 99999 http://127.0.0.1:45000/
echo 'a100'
ab -n 1000 -c 100 -r -k -s 99999 http://127.0.0.1:45000/

echo 't1'
ab -n 1000 -c 1 -r -k -s 99999 http://127.0.0.1:46000/
echo 't10'
ab -n 1000 -c 10 -r -k -s 99999 http://127.0.0.1:46000/
echo 't50'
ab -n 1000 -c 50 -r -k -s 99999 http://127.0.0.1:46000/
echo 't100'
ab -n 1000 -c 100 -r -k -s 99999 http://127.0.0.1:46000/