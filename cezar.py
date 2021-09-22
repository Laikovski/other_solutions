str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
      "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
      "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


alpha = 'abcdefghijklmnopqrstuvwxyz'
alphs = 'cdefghijklmnopqrstuvwxyzab'
new_str = ''

for i in str:
      if i in alpha:
            ind = alpha.index(i)
            new_str += alphs[ind]
      else:
            new_str += i

print(new_str)