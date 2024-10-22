import config

class Address:
    name = "xmr-address"
    title = "XMR Address"
    if config.XMRLANG == "JP":
        description = "設定されているXMRのアドレスを表示する"
    if config.XMRLANG == "EN":
        description = "Display the set XMR address"

class Balance:
    name = "xmr-balance"
    title = "XMR Balance"
    if config.XMRLANG == "JP":
        description = "現在のXMR残高を日本円で表示する"
    if config.XMRLANG == "EN":
        description = "Displays the current XMR balance in US dollars"

class Hashrate:
    name = "xmr-hashrate"
    title = "XMR Hashrate"
    if config.XMRLANG == "JP":
        description = "平均ハッシュレートを表示する hour=0の場合現在のハッシュレートを表示する"
    if config.XMRLANG == "EN":
        description = "Displays the average hashrate. hour=0 to display the current hashrate"
    def embed_description(hour: int, member: str, hashrate: float | int):
        if member:
            if hashrate:
                if config.JP:
                    return f"{member}のハッシュレートは{hashrate}H/sです"
                if config.XMRLANG == "EN":
                    return f"{member}'s hashrate is {hashrate}H/s"
            else:
                if config.XMRLANG == "JP":
                    return f"{member}はマイニングしていません"
                if config.XMRLANG == "EN":
                    return f"{member} is not mining"
        elif hour:
            if config.XMRLANG == "JP":
                return f"過去{hour}時間の平均ハッシュレートは{hashrate:.2f}H/sです"
            if config.XMRLANG == "EN":
                return f"The average hashrate for the past {hour} hours is {hashrate:.2f}H/s"
        else:
            if config.XMRLANG == "JP":
                return f"現在のハッシュレートは{hashrate:.2f}H/sです"
            if config.XMRLANG == "EN":
                return f"The current hashrate is {hashrate:.2f}H/s"

class Help:
    name = "xmr-help"
    title = "XMR Hashrate"
    if config.XMRLANG == "JP":
        description = "XMRボットのヘルプを表示する"
    if config.XMRLANG == "EN":
        description = "Displays the help for the XMR bot"

class Member:
    name = "xmr-member"
    title = "XMR Member"
    if config.XMRLANG == "JP":
        description = "現在マイニング中のメンバーを表示する"
    if config.XMRLANG == "EN":
        description = "Displays the current mining members"
