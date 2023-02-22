import { Component } from '@angular/core';


interface Food {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-search-job-category',
  templateUrl: './search-job-category.component.html',
  styleUrls: ['./search-job-category.component.css']
})
export class SearchJobCategoryComponent {

  foods: Food[] = [
    {value: 'steak-0', viewValue: 'Steak'},
    {value: 'pizza-1', viewValue: 'Pizza'},
    {value: 'tacos-2', viewValue: 'Tacos'},
  ];
}
