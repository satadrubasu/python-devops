
## Generate the public-Private key pair (OpenSSL)
 Generate the private key  
  > openssl genrsa -des3 -out private.pem 2048  
 
 Generate the Public Key  
  > openssl rsa -in private.pem -outform PEM -pubout -out public.pem
  
## Use they keys to encrypt/decrypt file
 - Cannot encrypt a filesize greater than the size used for key = 2048 (here)
 
 Encrypt using the public key  
  > openssl rsautl -encrypt -inkey public.pem -pubin -in sample.txt -out sample.ssl  
  
 Decrypt using the private key
  > openssl rsautl -decrypt -inkey private.pem -in sample.ssl -out sample_regen.txt 
  
  
  
  
  
  
  
