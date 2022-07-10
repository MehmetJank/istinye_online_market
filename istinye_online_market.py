#İstinye Üniversitesi BIL101 Temel Programlama 1 (Python) mini proje 3.
#"BIL101_Temel_Programlama_1_MP3.pdf" yönergesine göre yazılmıştır.

# ↓ Projemde yararlandığım bir kaynak bknz. satır 147 ve 152
# https://www.delftstack.com/howto/python/find-elements-with-specific-substring/

# ↓ Kullanıcının Faturasını Yazdırıken Tarihi yazdırmamızı sağlayan kütühaneye tanaımladım.
import datetime

# ↓ Kullanıcıların adı ve şifresinin bulunduğu dictonary.
users = {"user_1":"ahmet","user_1_pswd":"İstinye123","user_2":"meryem","user_2_pswd":"4444"}  

# ↓ Marketimizin stoğu burda dictonary olarak tanımlı.
stock = {"kuşkonmaz": [6,3], "brokoli": [20,7], "havuç": [15,5], "elmalar": [25,15],  
"muz": [19, 18], "meyve": [23,5], "yumurta": [44,4], "karışık meyve suyu": [1,19],
"balık çubukları": [27,10], "dondurma": [0,4], "elma suyu": [33,8], "portakal suyu": [32,4], "üzüm suyu": [21,16]}

user_1_cart = {}
user_2_cart = {}

# ↓ kullanıcının login olmasını sağlayan fonksiyon
def user_login():   
    global user_name
    user_name = str(input("Lütfen Kullanıcı adınızı girin:"))
    user_pswd = str(input("\nLütfen şifrenizi girin:"))
    
    # ↓ while döngüsü kullanarak kullanıcının kullanıcı adı ve şifresini kontrol ettim
    while (user_name != users["user_1"] or user_pswd != users["user_1_pswd"]) and (user_name != users["user_2"] or user_pswd != users["user_2_pswd"]):
        print("\nKullanici adiniz ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")
        user_name = str(input("\nLütfen isminizi girin:"))
        user_pswd = str(input("\nLütfen şifrenizi girin:"))

    print("\nBaşarıyla giriş yapıldı!")
    print(f"\nHoşgeldiniz {user_name} Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin\n")


cart = { }   # <- dictonary olarak kullanıcının sepeti

# ↓ herhangi listedeki her hangi bir indexe sahip indexi stringe donusturme fonksiyonu
def list_to_item(cart,a):   
    str_turned = str(cart[a])
    return str_turned

i = True
# ↓  Ana menü fonksiyonu diğer bütün fonksiyonlarla bağlantılıdır. 
def choice():
    global str_match,user_choice,cart,i
    # ↓ User login fonksiyonunu ilk başta çağırır (i ilk olarak True tanımlandığı için)
    if i:
        user_login()
    else:
        pass
    
    #  ↓ Yukarıda Tanımlı olan market stoğumuzda ürün var mı diye kontrol eder.
    def stock_check():        
        stock_number = stock[str_match[b]]
        stock_number_2 = stock_number[0]
        if adet == 0:
            print("Ana Menüye Yönlendiriliyorsunuz!\n")
        elif stock_number_2 < adet:
            print(f"Maksimum {stock_number_2} tane ürün giriniz!\nTekrar Deneyiniz!")
            return search_func()
        else:
            return True
    # ↓ Stoktan bir ürün bulup onu cart(sepet)ımıza akleyen fonksiyon.
    def search_func():
        global adet,b
        adet = 1
        b = user_choice -1
        a = list_to_item(str_match,b) 
        adet = int(input(f"\nSeçiminiz, {str_match[b]} Sepete Ekleniyor! Adet Giriniz (Ana menü için 0 girin): "))
        if stock_check():
            cart[a] = adet
            print(f"Sepetinize {a},{adet} tane eklendi!\nAna Menüye Yönlendiriliyorsunuz.\n")
            
    # ↓ Sepet Alt menüsü
    def cart_print():
        cart_print_2()
        cart_choice = int(input("Bir seçeneği seçiniz:\n1. Tutarı güncelleyin\n2. Bir öğeyi kaldırın\n3. Satın al\n4. ana menüye dön\n\nSeçiminiz: "))
        if cart_choice == 1:
            cart_changing = int(input("Lütfen miktarını değiştireceğiniz öğeyi seçin: "))
            value_at_index_2 = list(cart.keys())[cart_changing -1]
            print(value_at_index_2,"Seçildi")
            cart_available_new_value = int(input("Lütfen yeni miktarı yazın: "))
            cart[value_at_index_2] = cart_available_new_value
            print("Sepetiniz Güncellendi: \n")
            return cart_print()
        elif cart_choice == 2:
            cart_remove_choice = (int(input("Hangi Ürünü Kaldırmak İstiyorsunuz? ")))
            value_at_index_3 = list(cart.keys())[cart_remove_choice -1] 
            cart.pop(value_at_index_3)
            print(value_at_index_3,"Başarıyla Sepetinizden Kaldırıldı!")
            return cart_print()
        elif cart_choice == 3:
            print("Satın Alma Menüsüne Yönlendiriliyorsunuz.")
            buy()
        elif cart_choice == 4:
            return choice()
        else:   
            print(f"Seciminiz ile ilgili bir menü yok lütfen tekrardan seçim yapınız: ")
            return choice()
    
    # ↓ Sepetimizde hangi ürünler olduğunu yazdıran fonksiyon.
    def cart_print_2():
        cart_list_2 = []
        sayac_2 = 0
        index_2 = -1
        total = 0
        for key in cart.keys():
            cart_list_2.append(key)
            sayac_2 += 1
            index_2 += 1
            if key in cart_list_2:
                stock_price_2 = (stock[key][1])
                cart_available = cart[key]
                product = cart_available * stock_price_2
                total += product
                print(f"{sayac_2}-) {cart_list_2[index_2]} - birim fiyatı: {stock_price_2}$ sepetinizde {cart_available} tane var. Toplam = {product}$")
        print(f"Toplam sepet tutarı:{total}$\n")

    # ↓ Satın alma ve fatura yazdırma kısmı 
    def buy(): 
        index_4 = 0
        star = 12*"*"
        line = 60*"-"
        now = datetime.datetime.now()
        now_2 = now.strftime("%d-%m-%Y %H:%M:%S") # ← Zamanı yazdırmamızı sağlayan değişken
        for i in range(len(cart)):
            cart_keys = list(cart.keys())[index_4]
            cart_values = list(cart.values())[index_4]
            number_of_stock = (stock[cart_keys][0])
            number_of_price = (stock[cart_keys][1])
            index_4 += 1
            fatura_sonrasi = number_of_stock - cart_values
            stock[cart_keys] = [fatura_sonrasi,number_of_price]
            print(f"Makbuzunuz işleniyor ...\n\n{star} İstinye Online Market {star}\n{4*star}\n0850 283 6000\nistinye.edu.tr\n{line}")
            cart_print_2()
            print(f"{line}\n\n{now_2}\nOnline Market’imizi kullandığınız için teşekkür ederiz!\nAna menüye yönlendirilyorsunuz.\n")
        choice()

    # ↓ Ürün arama kısmında her ürünün fiyatını yazdıran fonksiyon.
    def price():
        fiyat = stock[str_match[index]]
        fiyat_2 = fiyat[1]
        return (fiyat_2)
    
    user_choice = int(input("Lütfen aşağıdaki hizmetlerden birini seçin: \n1. Ürün ara\n2. Sepete git\n3. Satın al\n4. Oturum Kapat\n5. Çıkış yap\n\nSeçiminiz: "))
    if user_choice == 1:
        while user_choice != 0:     #kullanıcı search menusu.
            ara = input("Ne arıyorsunuz?: ")
            str_match = [a for a in stock if str(ara.lower()) in a] 
            # ↓ Eğer aramadan hiç bir sonuç çıkmazsa veya kullanıcı "" ararsa kullanıcıdan tekrar arama yapmasını isteyen döngü
            while len(str_match) == 0 or ara =="": 
                print("Böyle bir sonuç Bulunamadı Lütfen Tekrar Arama Yapın! (Ana menü için 0 girin)")
                ara = input("Ne arıyorsunuz?: ")
                str_match = [a for a in stock if str(ara.lower()) in a]
                if ara == "0":
                    print("Ana menüye yönlendirilyorsunuz. \n")
                    # ara = input("Ne arıyorsunuz?: ")
                    i = False
                    return choice()

            print(len(str_match),"Tane Sonuç Bulundu! \nSonuçlar:")
            index = 0
            sayac = 1
            # ↓ Sonuçları yazdırmamızı sağlayan for döngüsü.
            for i in range(len(str_match)):
                if stock[str_match[index]][0]: 
                    print(sayac,"-)",str_match[index],price(),"$")
                else:
                    print(sayac,"-)",str_match[index],price(),"$","(Stokta yok!)")
                    
                index += 1
                sayac += 1
            user_choice = int(input("Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin): "))
            if user_choice == 0:
                i = False
                return choice()
            search_func()
            i = False
            return choice()
    elif user_choice == 2:
        cart_print()
    elif user_choice == 3:
        print(buy())
    elif user_choice == 4:
        i = True
        return choice()
    elif user_choice == 5:
        print(f"Seciminiz {user_choice}\nBizi tercih ettiğiniz için teşekkürler yine bekleriz!")
    else:
        print(f"\nSeciminiz {user_choice} ile ilgili bir menü yok lütfen tekrardan seçim yapınız: ")
        i = False
        return choice() 
choice() 

