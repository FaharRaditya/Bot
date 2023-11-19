import discord
import os
from discord.ext import commands
pertanyaan = 0

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    daftar = os.listdir("E:\\Pictures\\Roblox")
    for i in daftar:
        print(i)
        f = open('E:\\Pictures\\Roblox\\'+ i, 'rb')
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
        await ctx.send(file=picture)

@bot.command()
async def info_sampah(ctx):
    global pertanyaan
    pertanyaan = 1
    await ctx.send('''
Hai selamat datang di bot pengetahuan tentang 
Pilihlan beberapa pilihan tentang sampah di bawah ini
1. Mengapa sampah plastik dapat menggagu ekosistem?
2. Bagaimana cara mengatasi sampah plastik?
3. Bagaimana cara daur ulang sampah plastik?
4. Apa ciri ciri plastik yang gampang untuk di daur ulang?
                   
gunakan huruf p sebelum pilihan nomor, contoh : p1 untuk nomor 1
''')
@bot.command()
async def p1(ctx):
    if pertanyaan == 1:
        await ctx.send('''
    1. Sampah plastik dapat mengganggu ekosistem karena beberapa alasan utama:

2. Kerusakan Lingkungan Fisik: Plastik dapat mengakibatkan kerusakan fisik pada lingkungan. Ketika sampah plastik dibuang secara tidak tepat, seperti di sungai, lautan, atau tanah, plastik tersebut dapat menyumbat saluran air, merusak ekosistem sungai, dan menimbulkan bahaya bagi makhluk hidup di dalamnya.

3. Bahaya bagi Hewan: Hewan laut dan darat sering kali salah mengira sampah plastik sebagai makanan. Saat memakan plastik, hewan-hewan ini dapat mengalami cedera, keracunan, atau bahkan kematian. Selain itu, banyak hewan yang terperangkap atau terjerat di dalam plastik seperti jaring ikan atau hiasan plastik, menyebabkan cedera atau kematian.

4. Pencemaran Bahan Kimia Berbahaya: Plastik mengandung bahan kimia tertentu yang dapat terlepas ke lingkungan seiring waktu. Saat plastik terurai menjadi partikel-partikel yang lebih kecil (misalnya, mikroplastik), bahan kimia berbahaya seperti bisphenol A (BPA) atau ftalat dapat terlepas dan terbawa oleh air atau dimakan oleh organisme hidup, menyebabkan masalah kesehatan.
    ''')
    
@bot.command()
async def p2(ctx):
    if pertanyaan == 1:
        await ctx.send('''
    1. Menggunakan kantong belanja yang bahannya bukan dari plastik
    2. Membawa tumbler sendiri
    3. Daur ulang sampah plastik
    ''')
        
@bot.command()
async def p3(ctx):
    if pertanyaan == 1:
        await ctx.send('''
    1. Pemilahan Sampah: Pisahkan plastik dari sampah lainnya. Gunakan wadah atau tempat sampah terpisah untuk plastik agar lebih mudah didaur ulang.

2. Pembersihan Plastik: Bersihkan plastik dari kotoran atau sisa-sisa makanan. Pastikan untuk membersihkan dan mengeringkan plastik sebelum didaur ulang.

3. Identifikasi Jenis Plastik: Kenali kode daur ulang pada plastik (biasanya ditandai dengan simbol segitiga dengan angka di dalamnya). Kode ini membantu dalam proses pengelompokan dan daur ulang plastik yang sesuai.

4. Pemotongan atau Pemecahan: Beberapa plastik perlu dipotong atau diproses menjadi potongan-potongan kecil agar lebih mudah didaur ulang.
    ''')
        
@bot.command()
async def p4(ctx):
    if pertanyaan == 1:
        await ctx.send('''
    Penting untuk dicatat bahwa tidak semua jenis plastik dapat didaur ulang dengan mudah atau efisien. Beberapa plastik mungkin sulit untuk didaur ulang atau memerlukan proses yang lebih kompleks. Oleh karena itu, penting untuk melakukan pemilahan sampah yang tepat. Berikut adalah ciri cirinya
    1. Kode Daur Ulang: Plastik yang mudah didaur ulang biasanya memiliki kode daur ulang pada produknya. Kode ini biasanya terletak di dalam simbol segitiga yang menandai jenis plastik. Plastik dengan kode daur ulang tertentu, seperti PET (kode #1), HDPE (kode #2), dan LDPE (kode #4), cenderung lebih mudah didaur ulang dibandingkan dengan yang lain.

2. Bentuk dan Struktur: Plastik yang memiliki struktur seragam dan tidak tercampur dengan bahan lain, seperti label atau pewarna, cenderung lebih mudah untuk didaur ulang. Plastik dalam bentuk botol, wadah, atau kemasan yang terpisah dari bahan tambahan lainnya lebih mudah diproses dalam proses daur ulang.

3. Ketersediaan Pasar: Plastik yang memiliki permintaan pasar yang tinggi untuk didaur ulang biasanya lebih mudah diproses. Contohnya adalah botol air minum (biasanya terbuat dari PET) dan wadah plastik (biasanya terbuat dari HDPE) yang umumnya memiliki pasar daur ulang yang besar.

4. Kemurnian dan Kebersihan: Plastik yang lebih bersih dan tidak terkontaminasi dengan bahan lain memiliki kemungkinan lebih besar untuk didaur ulang. Plastik yang telah dibersihkan dengan baik dari sisa-sisa makanan atau benda asing lainnya akan lebih mudah diproses dalam fasilitas daur ulang.

5. Kemampuan untuk Didaur Ulang: Beberapa jenis plastik memiliki kemampuan yang lebih baik untuk didaur ulang daripada yang lain. Misalnya, polietilen (HDPE dan LDPE) cenderung lebih mudah didaur ulang daripada polistirena (PS) yang biasanya sulit didaur ulang.
    ''')
