
#define CURL_STATICLIB
#define LC_ALL 0
#include <iostream>
#include<string>
#include <windows.h>
#include "curl/curl.h"
#ifdef _DEBUG
#pragma comment (lib,"curl/libcurl_a_debug.lib")
#else
#pragma comment (lib,"curl/libcurl_a_.lib")
#endif
#pragma comment (lib,"Normaliz.lib")
#pragma comment (lib,"Ws2_32.lib")
#pragma comment (lib,"Wldap32.lib")
#pragma comment (lib,"Crypt32.lib")
#pragma comment (lib,"advapi32.lib")
using namespace std;
static size_t my_write(void* buffer, size_t size, size_t nmemb, void* param)
{
    string& text = *static_cast<string*>(param);
    size_t totalsize = size * nmemb;
    text.append(static_cast<char*>(buffer), totalsize);
    return totalsize;
}

int main()
{
    setlocale(LC_ALL, "Ressian");
    string result;
    CURL* curl;
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "https://home.mephi.ru/study_groups?term_id=12");
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, my_write);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &result);
        curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
        CURLcode code = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        if (CURLE_OK != code) {
            cerr << "CURL error: " << code << "\n";
        }
    }
    curl_global_cleanup();
    cout << result << "\n\n";
}

