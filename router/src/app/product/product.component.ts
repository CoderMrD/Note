import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '../../../node_modules/@angular/router';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  // 定义一个number，用来接收传递过来的id
  private productId:number;

  constructor(private routeInfo: ActivatedRoute) { }

  ngOnInit() {
    // 查询方式获取参数
    // this.productId = this.routeInfo.snapshot.queryParams["id"];

    // 路由路径方式获取参数，参数快照
    // this.productId = this.routeInfo.snapshot.params['id']

    // 路由路径获取参数，参数订阅
    this.routeInfo.params.subscribe((params:Params) => this.productId = params['id'])
  }

}
