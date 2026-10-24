export class ClinicClock {
  minute=480; paused=true; speed:1|2|4=1; fullDay=false; ended=false;
  constructor(fullDay=false){this.fullDay=fullDay}
  get label(){const h=Math.floor(this.minute/60),m=this.minute%60;return `${String(h%24).padStart(2,'0')}:${String(m).padStart(2,'0')}`}
  get endMinute(){return this.fullDay?1020:720}
  advance(minutes:number){if(this.ended||minutes<=0)return this.minute;this.minute=Math.min(this.minute+minutes,this.endMinute);if(this.fullDay&&this.minute>=720&&this.minute<780)this.minute=780;if(this.minute>=this.endMinute)this.ended=true;return this.minute}
  toggle(){if(!this.ended)this.paused=!this.paused}
  skip(minutes=15){this.advance(minutes)}
}
