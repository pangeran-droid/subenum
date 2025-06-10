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
    try:
        response = requests.get(site, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser").find_all("a")
        links = [link.get("href") for link in soup if link.get("href")]
        return links
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat mengakses situs: {e}")
        return []


def filter_valid_links(links):
    return [link for link in links if link.startswith("http://") or link.startswith("https://")]


def filter_by_domain(links, domain):
    return [link for link in links if urlparse(link).netloc.endswith(domain)]


def save_links_to_file(links, filename="hasil_links.txt"):
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
        print("\n🔗 Link yang ditemukan:")
        for idx, link in enumerate(filtered_links, 1):
            print(f"{idx}. {link}")
        
        save_links_to_file(filtered_links)
    else:
        print("⚠️ Tidak ada link yang sesuai filter.")
