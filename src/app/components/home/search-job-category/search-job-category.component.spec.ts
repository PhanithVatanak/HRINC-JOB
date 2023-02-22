import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchJobCategoryComponent } from './search-job-category.component';

describe('SearchJobCategoryComponent', () => {
  let component: SearchJobCategoryComponent;
  let fixture: ComponentFixture<SearchJobCategoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchJobCategoryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SearchJobCategoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
