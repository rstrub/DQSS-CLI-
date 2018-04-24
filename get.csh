#!/bin/csh

set mylist = $1
if ( "$mylist" == "" ) then 
   echo Expecting a filename with a list of data urls
   exit
endif

foreach f ( `cat url.list` )
  set url = `python driver.py $f`
  wget --content-disposition --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies "$url"
end
