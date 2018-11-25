# Applied Information Hiding Through Basic Encryption
## General Information
* Author: TJ Nel
* Date: 11/26/2018
* Description: This is a lesson plan that covers the basics of the security first principle, information hiding, using basic encryption

## Why You Should Care
Information Hiding is the process of attempting to prevent people from being able to see information. This is done to protect the information from being exposed to an unwanted party. Both defenders use this principle to forward their objectives. A defender may use information hiding to protect client formation on their servers from potential attackers. Conversely an attacker could use information hiding to prevent defenders from exposing their intentions. Infromation hiding is commonly used with in computer security. One of the more common uses of information hiding is encryption, encryption is the process of converting information or data info a code to prevent unauthorized access. Encryption is used within network communication protocols as well as data at rest. When someone comes across infromation that is encrypted it should not be unstandable.  The process of decrypting this information should be deteringly difficult for them with the encryption key or algorithm. This means those with the proper infromation should be able to easily transfer information without worry of third party eavesdropping.

There are 2 main types of encryption asymmetric and symmetric, symmetrical encryption uses the same key to encrypt and decrypt the data. While asymmetric uses 2 different keys for encryption a private key uses to encrypt the data and a public that can decrypt it. When using encryption it is important to never try to build you own algorithms because it is too easy to mistakenly introduce a security vulnerability to your alorigthm thereby allowing attackers to expose your information through cryptoanalysis. Many of the current encryption algorithms have been tested rigorously over the years and have proven resilient, but even those alorgithms eventually get broken. SHA-1 is a good example of a broken encryption algorithm, which is a hash generating algorithm used to create a checksum of files. SHA-1 has been deprecated by NIST in 2011 and since then an attack called [shattered](http://shattered.io) can be used to craft colliding documents.

### Examples of information hiding
#### Good Information Hiding

End to End Encryption

![End-to-End-Encryption](http://algoworksupload.s3.amazonaws.com/new-algoworks/wp-content/uploads/2016/08/31133326/End-to-End-Encryption-.jpg)

Symmetric Key Encryption

![symmEnc](https://www.ibm.com/support/knowledgecenter/en/SSB23S_1.1.0.14/gtps7/ssldig01.gif)

PGP encryption used for emails

![pgp](https://fedoramagazine.org/wp-content/uploads/2016/02/gpg-clearsign-example.png)

#### Bad Information Hiding

Guessable Password... Thanks Kanye

![kanyes password](http://www.break.com/wp-content/uploads/2018/10/kanye.jpg)

Passwords in plain text

![smtp_pass](https://www.drupal.org/files/issues/smtp.png)

## Three Main Ideas
1.  Data can be considered very important and senstive thus making it worthwhile to be kept private, the act of information hiding allows you to protect said data.
2.  Encryption is one of the main uses of information hiding it can protect data in transit and at rest.
3.  Encryption is very hard to create and is constantly tested, if weak encryption is implemented attackers can break it with cryptoanlysis and gain access to your data.

## Future Direction
This topic can be explored further by looking into additional encryption algorithms and cryptoanalysis attacks such as RSA and the hastad broadcast attack. Implementations like these often find their way into Security CTF challenges so particpation in CTFs will improve you understanding in this topic. Another good resource is https://cryptopals.com/ which his a series of challanges that will require you to master cryptography the overarching principle of encryption.

## Additional Resources
* [Lesson Video (10Min)](http://)
* [Cryptopals](https://cryptopals.com/)
* [Serious Cryptography Book](https://nostarch.com/seriouscrypto)
