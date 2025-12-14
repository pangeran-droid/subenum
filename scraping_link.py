try:
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urlparse
except ImportError as e:
    print("❌ Ada modul yang belum terinstal:", e)
    print("💡 Jalankan perintah berikut untuk menginstalnya:")
    print("   pip install -r requirements.txt")
    exit(1)


def extract_all_links(site):
    """Mengambil semua link dari halaman web"""
    try:
        response = requests.get(site, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = [link.get("href") for link in soup.find_all("a") if link.get("href")]
        return links
    except requests.exceptions.RequestException as e:
        print(f"❌ Terjadi kesalahan saat mengakses situs: {e}")
        return []


def filter_valid_links(links):
    """Filter link yang valid (http / https)"""
    return [link for link in links if link.startswith("http://") or link.startswith("https://")]


def filter_by_domain(links, domain):
    """Filter link berdasarkan domain tertentu"""
    return [link for link in links if urlparse(link).netloc.endswith(domain)]


def check_link_status(link):
    """Cek status HTTP link, kembalikan kode status dan teks"""
    try:
        r = requests.head(link, allow_redirects=True, timeout=5)
        return r.status_code, r.reason
    except requests.RequestException:
        return None, "Gagal"


def save_links_to_file(links, filename="hasil_links.txt"):
    """Simpan link ke file"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for link in links:
                file.write(link + "\n")
        print(f"\n✅ Link berhasil disimpan di file '{filename}'")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menyimpan file: {e}")


if __name__ == "__main__":
    site_link = input("Masukan URL (contoh: https://example.com) : ").strip()
    if not site_link.startswith("http"):
        site_link = "http://" + site_link

    domain_filter = input("Masukkan nama domain untuk filter (kosongkan jika tidak ingin filter domain, contoh: example.com) : ").strip()

    all_links = extract_all_links(site_link)
    valid_links = filter_valid_links(all_links)

    if domain_filter:
        filtered_links = filter_by_domain(valid_links, domain_filter)
    else:
        filtered_links = valid_links

    if filtered_links:
        print("\n🔗 Link yang ditemukan beserta status HTTP:")
        final_links = []
        for idx, link in enumerate(filtered_links, 1):
            code, reason = check_link_status(link)
            status_text = f"{code} {reason}" if code else "❌ Gagal"
            print(f"{idx}. {link} -> {status_text}")
            if code == 200:
                final_links.append(link)  # Hanya simpan link 200 OK

        save_links_to_file(final_links)
    else:
        print("⚠️ Tidak ada link yang sesuai filter.")
