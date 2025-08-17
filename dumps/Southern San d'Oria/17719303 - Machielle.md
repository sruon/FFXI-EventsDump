# 17719303 - Machielle

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 388 bytes                     |
| Total Events     | 3                             |
| References Count | 25                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [0](#event-0)         | 0x0001       |      1 |              1 |
| [512](#event-512)     | 0x0002       |    255 |             65 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FFC      |        8188 |
|       1 | 0x0000      |           0 |
|       2 | 0x1FFD      |        8189 |
|       3 | 0x0001      |           1 |
|       4 | 0x1FFE      |        8190 |
|       5 | 0x0002      |           2 |
|       6 | 0x1FFF      |        8191 |
|       7 | 0x0003      |           3 |
|       8 | 0x2000      |        8192 |
|       9 | 0x0004      |           4 |
|      10 | 0x2001      |        8193 |
|      11 | 0x0005      |           5 |
|      12 | 0x2002      |        8194 |
|      13 | 0x0006      |           6 |
|      14 | 0x2003      |        8195 |
|      15 | 0x0007      |           7 |
|      16 | 0x2004      |        8196 |
|      17 | 0x0008      |           8 |
|      18 | 0x2005      |        8197 |
|      19 | 0x0009      |           9 |
|      20 | 0x2006      |        8198 |
|      21 | 0x000A      |          10 |
|      22 | 0x2007      |        8199 |
|      23 | 0x000B      |          11 |
|      24 | 0x2008      |        8200 |

## String References

- **8188**: HI*%~5"H [$3I[$3L$3b$3V$3$5$3A$3b$3N$3X/$3R$3E$3$3$2L%e/$q [~$21$O]$3t$3$3O/$P13hh$P16rL [s$P15r/$3V$3F$3$1[$3 [$P10lL$5/%$3L$q$|h/ [~$21P%{$C%9$X/$3_$3{$3C$P122$8$P15q$16$17/R$17%qh$.%9/$26$3~$3b$3V$3/$3$3t$3$3O$9$z%;/$3_$3{$3C$P10v$P13|)g [AAD+=/$3N$3$3X$3^$3 [$3o$3X]
- **8189**: $3I[$3L$3b$3V$3$5$3A$3b$3N$3X>KB $3e$3X$3g%p>)g$2228813gH"fB
- **8190**: $3R$3E$3$3$2L%e>KB $3e$3X$3g%p>)g$2228813gH"fB
- **8191**: $q [p [~$215=1FI5=fB/$3e$3X$3g%p>)g$2228813gH"fB]
- **8192**: $P13hh$P16rL [s$P15r>KB/$3e$3X$3g%p>)g$2228813gH"fB]
- **8193**: $3V$3F$3$1[$3 [$P10lL$5>KB/$3e$3X$3g%p>)g$2228813gH"fB]
- **8194**: %$3L$q$|h>KB $3e$3X$3g%p>)g$2228813gH"fB
- **8195**: [~$21P%{$C%9$X>KB/$3e$3X$3g%p>)g$2228813gH"fB]
- **8196**: $3_$3{$3C$P122$8$P15q$16$17>KB $3e$3X$3g%p>)g$2228813gH"fB
- **8197**: R$17%qAD+=1FI5=fB $3e$3X$3g%p>)g$2228813gH"fB
- **8198**: $3~$3b$3V$3 $3$3t$3$3O$9$z%;>KB $3e$3X$3g%p>)g$2228813gH"fB
- **8199**: $3_$3{$3C$3$39983031FI5=fB $3e$3X$3g%p>)g$2228813gH"fB
- **8200**: $3N$3$3X$3^$3 [$3o$3X>KBi$3r$3\`$3r$3\`j/$3e$3X$3g%p>)g$2228813gH"fB]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 512

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 255 bytes |
| Instructions | 65        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 24  00 80 01 80 01 80 25 02    .....$......%.
0010: 00 10 01 80 00 23 00 1D  02 80 23 03 01 10 01 80  .....#....#.....
0020: 01 FF 00 02 00 10 03 80  00 37 00 1D 04 80 23 03  .........7....#.
0030: 01 10 03 80 01 FF 00 02  00 10 05 80 00 4B 00 1D  .............K..
0040: 06 80 23 03 01 10 05 80  01 FF 00 02 00 10 07 80  ..#.............
0050: 00 5F 00 1D 08 80 23 03  01 10 07 80 01 FF 00 02  ._....#.........
0060: 00 10 09 80 00 73 00 1D  0A 80 23 03 01 10 09 80  .....s....#.....
0070: 01 FF 00 02 00 10 0B 80  00 87 00 1D 0C 80 23 03  ..............#.
0080: 01 10 0B 80 01 FF 00 02  00 10 0D 80 00 9B 00 1D  ................
0090: 0E 80 23 03 01 10 0D 80  01 FF 00 02 00 10 0F 80  ..#.............
00A0: 00 AF 00 1D 10 80 23 03  01 10 0F 80 01 FF 00 02  ......#.........
00B0: 00 10 11 80 00 C3 00 1D  12 80 23 03 01 10 11 80  ..........#.....
00C0: 01 FF 00 02 00 10 13 80  00 D7 00 1D 14 80 23 03  ..............#.
00D0: 01 10 13 80 01 FF 00 02  00 10 15 80 00 EB 00 1D  ................
00E0: 16 80 23 03 01 10 15 80  01 FF 00 02 00 10 17 80  ..#.............
00F0: 00 FF 00 1D 18 80 23 03  01 10 17 80 01 FF 00 21  ......#........!
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x24] CREATE_DIALOG(message_id=8188*, default_option=0*, option_flags=0*)
    → "HI*%~5"H [$3I[$3L$3b$3V$3$5$3A$3b$3N$3X/$3R$3E$3$3$2L%e/$q [~$21$O]$3t$3$3O/$P13hh$P16rL [s$P15r/$3V$3F$3$1[$3 [$P10lL$5/%$3L$q$|h/ [~$21P%{$C%9$X/$3_$3{$3C$P122$8$P15q$16$17/R$17%qh$.%9/$26$3~$3b$3V$3/$3$3t$3$3O$9$z%;/$3_$3{$3C$P10v$P13|)g [AAD+=/$3N$3$3X$3^$3 [$3o$3X]"
  2: 0x000E [0x25] WAIT_DIALOG_SELECT()
  3: 0x000F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0023
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8189*)
    → "$3I[$3L$3b$3V$3$5$3A$3b$3N$3X>KB $3e$3X$3g%p>)g$2228813gH"fB"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x03] Work_Zone[1] = 0*
  7: 0x0020 [0x01] GOTO 0x00FF
  8: 0x0023 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0037
  9: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=8190*)
    → "$3R$3E$3$3$2L%e>KB $3e$3X$3g%p>)g$2228813gH"fB"
 10: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x002F [0x03] Work_Zone[1] = 1*
 12: 0x0034 [0x01] GOTO 0x00FF
 13: 0x0037 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x004B
 14: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=8191*)
    → "$q [p [~$215=1FI5=fB/$3e$3X$3g%p>)g$2228813gH"fB]"
 15: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0043 [0x03] Work_Zone[1] = 2*
 17: 0x0048 [0x01] GOTO 0x00FF
 18: 0x004B [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x005F
 19: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=8192*)
    → "$P13hh$P16rL [s$P15r>KB/$3e$3X$3g%p>)g$2228813gH"fB]"
 20: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0057 [0x03] Work_Zone[1] = 3*
 22: 0x005C [0x01] GOTO 0x00FF
 23: 0x005F [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0073
 24: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=8193*)
    → "$3V$3F$3$1[$3 [$P10lL$5>KB/$3e$3X$3g%p>)g$2228813gH"fB]"
 25: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x006B [0x03] Work_Zone[1] = 4*
 27: 0x0070 [0x01] GOTO 0x00FF
 28: 0x0073 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0087
 29: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=8194*)
    → "%$3L$q$|h>KB $3e$3X$3g%p>)g$2228813gH"fB"
 30: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x007F [0x03] Work_Zone[1] = 5*
 32: 0x0084 [0x01] GOTO 0x00FF
 33: 0x0087 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x009B
 34: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=8195*)
    → "[~$21P%{$C%9$X>KB/$3e$3X$3g%p>)g$2228813gH"fB]"
 35: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x0093 [0x03] Work_Zone[1] = 6*
 37: 0x0098 [0x01] GOTO 0x00FF
 38: 0x009B [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00AF
 39: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8196*)
    → "$3_$3{$3C$P122$8$P15q$16$17>KB $3e$3X$3g%p>)g$2228813gH"fB"
 40: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x00A7 [0x03] Work_Zone[1] = 7*
 42: 0x00AC [0x01] GOTO 0x00FF
 43: 0x00AF [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x00C3
 44: 0x00B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8197*)
    → "R$17%qAD+=1FI5=fB $3e$3X$3g%p>)g$2228813gH"fB"
 45: 0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x00BB [0x03] Work_Zone[1] = 8*
 47: 0x00C0 [0x01] GOTO 0x00FF
 48: 0x00C3 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x00D7
 49: 0x00CB [0x1D] PRINT_EVENT_MESSAGE(message_id=8198*)
    → "$3~$3b$3V$3 $3$3t$3$3O$9$z%;>KB $3e$3X$3g%p>)g$2228813gH"fB"
 50: 0x00CE [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x00CF [0x03] Work_Zone[1] = 9*
 52: 0x00D4 [0x01] GOTO 0x00FF
 53: 0x00D7 [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x00EB
 54: 0x00DF [0x1D] PRINT_EVENT_MESSAGE(message_id=8199*)
    → "$3_$3{$3C$3$39983031FI5=fB $3e$3X$3g%p>)g$2228813gH"fB"
 55: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x00E3 [0x03] Work_Zone[1] = 10*
 57: 0x00E8 [0x01] GOTO 0x00FF
 58: 0x00EB [0x02] IF !(Work_Zone[0] == 11*) GOTO 0x00FF
 59: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8200*)
    → "$3N$3$3X$3^$3 [$3o$3X>KBi$3r$3`$3r$3`j/$3e$3X$3g%p>)g$2228813gH"fB]"
 60: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 61: 0x00F7 [0x03] Work_Zone[1] = 11*
 62: 0x00FC [0x01] GOTO 0x00FF

SUBROUTINE_00FF:
 63: 0x00FF [0x21] END_EVENT
 64: 0x0100 [0x00] END_REQSTACK()
```
