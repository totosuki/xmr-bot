class Address:
    name = "xmr-address"
    title = "XMR Address"
    description = "設定されているXMRのアドレスを表示します"

class Balance:
    name = "xmr-balance"
    title = "XMR Balance"
    description = "現在のXMR残高を日本円で表示します"

class Hashrate:
    name = "xmr-hashrate"
    title = "XMR Hashrate"
    description = "平均ハッシュレートを表示する hour = 0 にすると現在のハッシュレートを表示する"
    def embed_description(hour: int, member: str, hashrate: float | int):
        if member:
            if hashrate:
                return f"{member}のハッシュレートは{hashrate}H/sです"
            else:
                return f"{member}はマイニングしていません"
        elif hour:
            return f"過去{hour}時間の平均ハッシュレートは{hashrate:.2f}H/sです"
        else:
            return f"現在のハッシュレートは{hashrate:.2f}H/sです"

class Help:
    name = "xmr-help"
    title = "XMR Hashrate"
    description = "XMRボットのヘルプを表示する"

class Member:
    name = "xmr-member"
    title = "XMR Member"
    description = "現在マイニング中のメンバーを表示する"