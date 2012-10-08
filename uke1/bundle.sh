#/bin/sh

s1=$1
s2=$2
s=$(find $s1 -name $s2 -print)

for i in $s; do
	echo "echo unpacking file $i"
	echo "cat > $i <<EOF"
	cat $i
	echo "EOF"
done

#fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke1$ ./bundle.sh ~/uio/#inf3331 *.txt
#echo unpacking file /home/fredrik/uio/inf3331/test/gress4.txt
#cat > /home/fredrik/uio/inf3331/test/gress4.txt <<EOF
#grønt
#EOF
#echo unpacking file /home/fredrik/uio/inf3331/test/gress5.txt
#cat > /home/fredrik/uio/inf3331/test/gress5.txt <<EOF
#gress!!!!!!
#EOF
#echo unpacking file /home/fredrik/uio/inf3331/test/gress3.txt
#cat > /home/fredrik/uio/inf3331/test/gress3.txt <<EOF
#masse
#EOF
#echo unpacking file /home/fredrik/uio/inf3331/test/gress2.txt
#cat > /home/fredrik/uio/inf3331/test/gress2.txt <<EOF
#spiser
#EOF
#echo unpacking file /home/fredrik/uio/inf3331/test/gress1.txt
#cat > /home/fredrik/uio/inf3331/test/gress1.txt <<EOF
#kuen
#EOF
