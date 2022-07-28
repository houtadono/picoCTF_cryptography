from Crypto.Util.number import long_to_bytes

# **note: with this challenge: n,e,ciphertext dependent Oracle 
n = 96696903097183458361402733459936511417781756664882602569670327738449654297366747575614591581560950963488079341812117378849852166388208072323652963745729034957784264126404909758345308823183700492236209271744978219463575417766755692450813626202292185300481549386277650001091918677944481795428035993474073875127
e = 65537
ciphertext = 28029731341869576826532820101938392244220608463625339771805711999528503246282849059662580860039826864161042159307974150708642544034565896945556471533484183669414020059996325137810325936065072648718763767403679477204502363838311712139908862013895001160809079706639074460439089333439819568239217182949091268537

# encrypt m1 * encrypt m2 = (m1*m2) ** e mod n = c1 * c2
# => decrypt(c1*c2 )= m1*m2

# we have c1; find m1 = m1 * m2 /m2 = decrypt(c1*c2 ) /m2
# from m2 into c2 , we calculator c1*c2 and using Oracle find m1*m2

message2 = 2
ciphertext2 = pow(2,e,n)
ciphertext12 = ciphertext2*ciphertext 
# print(ciphertext12)
# send ciphertext12 to Oracle find m12
message12 = 580550060391700078946913236734911770139931497702556153513487440893406629034802718534645538074938502890769425795379846471930
message = message12//message2

print(long_to_bytes(message).decode())



