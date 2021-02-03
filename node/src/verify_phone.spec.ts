import Axios from 'axios'
import * as qs from 'qs'
import * as dotenv from 'dotenv'

const logger = console
dotenv.config()
const appcode = process.env.APPCODE

describe('verify_phone', () => {
  /**
   * 贵州数据宝网络科技有限公司
   * @link https://market.aliyun.com/products/57126001/cmapi00035240.html
   */
  test.skip('sjsys', async () => {
    const url = 'http://sjsys.market.alicloudapi.com/communication/personal/1979'
    const res = await Axios.post(url, qs.stringify({
      idcard: '32132419860817421X',
      mobile: '13636643334',
      name: '张三'
    }), {
      headers: {
        Authorization: `APPCODE ${appcode}`,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      }
    })
    logger.info(`res status ${res.status}, data ${JSON.stringify(res.data)}`)
  })

  /**
   * 杭州数脉科技有限公司
   * @link https://market.aliyun.com/products/57000002/cmapi026100.html
   */
  test('shumaidata', async () => {
    const url = 'https://mobile3elements.shumaidata.com/mobile/verify_real_name'
    const res = await Axios.post(url, qs.stringify({
      idcard: '32132419860817421X',
      mobile: '13636643334',
      name: '张三'
    }), {
      headers: {
        Authorization: `APPCODE ${appcode}`,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      }
    })
    logger.info(`res status ${res.status}, data ${JSON.stringify(res.data)}`)
  })
})
