import os

print("Select the version of macOS you want to download")
print("1: Lion")
print("2: Mountain Lion")
print("3: Mavericks")
print("4: Yosemite")
print("5: El Capitan")
print("6: Sierra")
print("7: High Sierra")
print("8: Mojave")
print("9: Catalina")
print("10: Big Sur")
print("11: Monterey")
osxver = input("Enter Version: ")


if osxver == 1:
  os.system("python macrecovery.py -b Mac-2E6FAB96566FE58C -m 00000000000F25Y00 download")
elif osxver == 2:
  os.system("python macrecovery.py -b Mac-7DF2A3B5E5D671ED -m 00000000000F65100 download")
elif osxver == 3:
  os.system("python macrecovery.py -b Mac-F60DEB81FF30ACF6 -m 00000000000FNN100 download")
elif osxver == 4:
  os.system("python macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000GDVW00 download")
elif osxver == 5:
  os.system("python macrecovery.py -b Mac-FFE5EF870D7BA81A -m 00000000000GQRX00 download")
elif osxver == 6:
  os.system("python macrecovery.py -b Mac-77F17D7DA9285301 -m 00000000000J0DX00 download")
elif osxver == 7:
  os.system("python macrecovery.py -b Mac-7BA5B2D9E42DDD94 -m 00000000000J80300 download")
elif osxver == 8:
  os.system("python macrecovery.py -b Mac-7BA5B2DFE22DDD8C -m 00000000000KXPG00 download")
elif osxver == 9:
 os.system(" python macrecovery.py -b Mac-00BE6ED71E35EB86 -m 00000000000000000 download")
elif osxver == 10:
 os.system(" python macrecovery.py -b Mac-42FD25EABCABB274 -m 00000000000000000 download")
elif osxver == 11:
 os.system(" python python macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000000000 download")