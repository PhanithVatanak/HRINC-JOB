import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HomeMainJobComponent } from './home-main-job.component';

describe('HomeMainJobComponent', () => {
  let component: HomeMainJobComponent;
  let fixture: ComponentFixture<HomeMainJobComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HomeMainJobComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HomeMainJobComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
