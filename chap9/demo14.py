s = '评书新势力'
# 编码
print(s.encode(encoding='GBK'))  # 在 GBK 这种编码格中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在 UTF-8 这种编码格中，一个中文占三个字节

# 解码
# byte 代表就是一个二进制数据（字节类型的数据）
byte = s.encode(encoding='GBK')  # 编码
print(byte.decode(encoding='GBK'))  # 解码

byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
