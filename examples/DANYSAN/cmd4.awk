#!/bin/gawk

# cuento los numeros con cero frecuencia.

BEGIN {
	for( i = 0 ; i < 1000; i++ )
	{
		frq[i] = 0;
	}

}

{
	a = strtonum($0);
	frq[a]++;	

}

END {
#	for (i = 0 ; i < 1000; i++ )
#	{
#		if( frq[i] == 0 ) printf ( "%d = %d\n", i, frq[i] );
#	}

	for( i = 0 ; i < 1000; i++)
	{
		#if( frq[i] != 0 ) printf ( "%d = %d\n", i, frq[i] );
		printf ( "%03d = %d\n", i, frq[i] );
	}
}
