# 17473708 - IZUMI of MANGETSU

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 740 bytes                    |
| Total Events     | 13                           |
| References Count | 13                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [42](#event-42)          | 0x0001       |    555 |             67 |
| [43](#event-43)          | 0x022C       |     14 |              2 |
| [44](#event-44)          | 0x023A       |      1 |              1 |
| [45](#event-45)          | 0x023B       |     14 |              2 |
| [46](#event-46)          | 0x0249       |     14 |              2 |
| [65535.1](#event-655351) | 0x0257       |      1 |              1 |
| [48](#event-48)          | 0x0258       |     14 |              2 |
| [49](#event-49)          | 0x0266       |      1 |              1 |
| [1](#event-1)            | 0x0267       |      1 |              1 |
| [50](#event-50)          | 0x0268       |      1 |              1 |
| [32000](#event-32000)    | 0x0269       |      1 |              1 |
| [32001](#event-32001)    | 0x026A       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C94      |        7316 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
|       6 | 0x0005      |           5 |
|       7 | 0x0006      |           6 |
|       8 | 0x001E      |          30 |
|       9 | 0x0007      |           7 |
|      10 | 0x00C8      |         200 |
|      11 | 0x003C      |          60 |
|      12 | 0x1C95      |        7317 |

## String References

- **7316**: $30L$P10r$3G$3t$3F$3N$3g$3e$3X$3g$0$P16Z [$P10^A$21$P10ri$3f$3t$3H$4853290ADi$s$P11T/$21$P12u$P11f1$P12i$K/$21$P12u$P11f2$P12i$K/$P10r*$P13'+F(i$4981341 [V$./$3G$3t$3F$3N$3g$3$3Z$3b$3g/endmapschedulori$9$z%;j]
- **7317**: $3{$3^$3$97F$3f$3$I%9B

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

### Event 42

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 555 bytes |
| Instructions | 67        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 2E   $......%.......
0010: 00 2D F8 FF FF 7F F8 FF  FF 7F 68 61 65 64 2D F8  .-........haed-.
0020: FF FF 7F F8 FF FF 7F 6B  72 6F 69 01 C4 01 02 00  .......kroi.....
0030: 10 02 80 00 4D 00 29 01  AA A0 0A 01 03 2D F8 FF  ....M.)......-..
0040: FF 7F F8 FF FF 7F 68 73  68 69 01 C4 01 02 00 10  ......hshi......
0050: 03 80 00 6C 00 29 01 AB  A0 0A 01 03 2D F8 FF FF  ...l.)......-...
0060: 7F F8 FF FF 7F 6B 69 6B  61 01 C4 01 02 00 10 04  .....kika.......
0070: 80 00 84 00 2D F8 FF FF  7F F8 FF FF 7F 6B 69 6B  ....-........kik
0080: 62 01 C4 01 02 00 10 05  80 00 A9 00 2D F8 FF FF  b...........-...
0090: 7F F8 FF FF 7F 69 7A 75  6D 2D F8 FF FF 7F F8 FF  .....izum-......
00A0: FF 7F 68 61 73 74 01 C4  01 02 00 10 06 80 00 C1  ..hast..........
00B0: 00 2D F8 FF FF 7F F8 FF  FF 7F 79 6F 6D 69 01 C4  .-........yomi..
00C0: 01 02 00 10 07 80 00 2E  01 2D F8 FF FF 7F F8 FF  .........-......
00D0: FF 7F 6B 69 6C 6B 2D F8  FF FF 7F F8 FF FF 7F 6B  ..kilk-........k
00E0: 69 6C 68 29 01 AA A0 0A  01 04 1C 08 80 2D F8 FF  ilh).........-..
00F0: FF 7F F8 FF FF 7F 6B 69  6C 61 29 01 AB A0 0A 01  ......kila).....
0100: 04 1C 08 80 2D F8 FF FF  7F F8 FF FF 7F 6B 69 6C  ....-........kil
0110: 69 2D F8 FF FF 7F F8 FF  FF 7F 68 61 65 64 2D F8  i-........haed-.
0120: FF FF 7F F8 FF FF 7F 6B  69 6C 79 01 C4 01 02 00  .......kily.....
0130: 10 09 80 00 C4 01 45 0A  80 F0 FF FF 7F F0 FF FF  ......E.........
0140: 7F 66 64 6F 31 01 80 51  F0 FF FF 7F F0 FF FF 7F  .fdo1..Q........
0150: 68 73 68 69 1C 0B 80 51  F0 FF FF 7F F0 FF FF 7F  hshi...Q........
0160: 6B 69 6B 61 1C 0B 80 51  F0 FF FF 7F F0 FF FF 7F  kika...Q........
0170: 69 7A 75 6D 1C 0B 80 51  F0 FF FF 7F F0 FF FF 7F  izum...Q........
0180: 79 6F 6D 69 1C 0B 80 45  0A 80 F0 FF FF 7F F0 FF  yomi...E........
0190: FF 7F 66 64 69 31 01 80  48 0C 80 23 45 0A 80 F0  ..fdi1..H..#E...
01A0: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 1C 0B 80  .......fdo1.....
01B0: 45 0A 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
01C0: 80 01 C4 01 48 0C 80 23  2D F8 FF FF 7F F8 FF FF  ....H..#-.......
01D0: 7F 6B 69 6C 6B 2D F8 FF  FF 7F F8 FF FF 7F 6B 69  .kilk-........ki
01E0: 6C 68 29 01 AA A0 0A 01  04 1C 08 80 2D F8 FF FF  lh).........-...
01F0: 7F F8 FF FF 7F 6B 69 6C  61 29 01 AB A0 0A 01 04  .....kila)......
0200: 1C 08 80 2D F8 FF FF 7F  F8 FF FF 7F 6B 69 6C 69  ...-........kili
0210: 2D F8 FF FF 7F F8 FF FF  7F 68 61 65 64 2D F8 FF  -........haed-..
0220: FF 7F F8 FF FF 7F 6B 69  6C 79 21 00              ......kily!.    
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7316*, default_option=0*, option_flags=0*)
    → "$30L$P10r$3G$3t$3F$3N$3g$3e$3X$3g$0$P16Z [$P10^A$21$P10ri$3f$3t$3H$4853290ADi$s$P11T/$21$P12u$P11f1$P12i$K/$21$P12u$P11f2$P12i$K/$P10r*$P13'+F(i$4981341 [V$./$3G$3t$3F$3N$3g$3$3Z$3b$3g/endmapschedulori$9$z%;j]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002E
  3: 0x0011 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "haed" with entities [EventEntity, EventEntity]
  4: 0x001E [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kroi" with entities [EventEntity, EventEntity]
  5: 0x002B [0x01] GOTO 0x01C4
  6: 0x002E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004D
  7: 0x0036 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Water in Space (ID: 17473706/0x010AA0AA), tag_num=0x03)
  8: 0x003D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "hshi" with entities [EventEntity, EventEntity]
  9: 0x004A [0x01] GOTO 0x01C4
 10: 0x004D [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x006C
 11: 0x0055 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=POWDER (ID: 17473707/0x010AA0AB), tag_num=0x03)
 12: 0x005C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kika" with entities [EventEntity, EventEntity]
 13: 0x0069 [0x01] GOTO 0x01C4
 14: 0x006C [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0084
 15: 0x0074 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kikb" with entities [EventEntity, EventEntity]
 16: 0x0081 [0x01] GOTO 0x01C4
 17: 0x0084 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x00A9
 18: 0x008C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "izum" with entities [EventEntity, EventEntity]
 19: 0x0099 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "hast" with entities [EventEntity, EventEntity]
 20: 0x00A6 [0x01] GOTO 0x01C4
 21: 0x00A9 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00C1
 22: 0x00B1 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "yomi" with entities [EventEntity, EventEntity]
 23: 0x00BE [0x01] GOTO 0x01C4
 24: 0x00C1 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x012E
 25: 0x00C9 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kilk" with entities [EventEntity, EventEntity]
 26: 0x00D6 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kilh" with entities [EventEntity, EventEntity]
 27: 0x00E3 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Water in Space (ID: 17473706/0x010AA0AA), tag_num=0x04)
 28: 0x00EA [0x1C] WAIT(30* ticks)
 29: 0x00ED [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kila" with entities [EventEntity, EventEntity]
 30: 0x00FA [0x29] REQ_SET_WAIT(priority=0x01, entity_id=POWDER (ID: 17473707/0x010AA0AB), tag_num=0x04)
 31: 0x0101 [0x1C] WAIT(30* ticks)
 32: 0x0104 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kili" with entities [EventEntity, EventEntity]
 33: 0x0111 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "haed" with entities [EventEntity, EventEntity]
 34: 0x011E [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kily" with entities [EventEntity, EventEntity]
 35: 0x012B [0x01] GOTO 0x01C4
 36: 0x012E [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x01C4
 37: 0x0136 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x0147 [0x51] END_MAP_SCHEDULER: End scheduler "hshi" with entities [LocalPlayer, LocalPlayer]
 39: 0x0154 [0x1C] WAIT(60* ticks)
 40: 0x0157 [0x51] END_MAP_SCHEDULER: End scheduler "kika" with entities [LocalPlayer, LocalPlayer]
 41: 0x0164 [0x1C] WAIT(60* ticks)
 42: 0x0167 [0x51] END_MAP_SCHEDULER: End scheduler "izum" with entities [LocalPlayer, LocalPlayer]
 43: 0x0174 [0x1C] WAIT(60* ticks)
 44: 0x0177 [0x51] END_MAP_SCHEDULER: End scheduler "yomi" with entities [LocalPlayer, LocalPlayer]
 45: 0x0184 [0x1C] WAIT(60* ticks)
 46: 0x0187 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x0198 [0x48] [System] [7317*]:
    → "$3{$3^$3$97F$3f$3$I%9B"
 48: 0x019B [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x019C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x01AD [0x1C] WAIT(60* ticks)
 51: 0x01B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 52: 0x01C1 [0x01] GOTO 0x01C4

SUBROUTINE_01C4:
 53: 0x01C4 [0x48] [System] [7317*]:
    → "$3{$3^$3$97F$3f$3$I%9B"
 54: 0x01C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x01C8 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kilk" with entities [EventEntity, EventEntity]
 56: 0x01D5 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kilh" with entities [EventEntity, EventEntity]
 57: 0x01E2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Water in Space (ID: 17473706/0x010AA0AA), tag_num=0x04)
 58: 0x01E9 [0x1C] WAIT(30* ticks)
 59: 0x01EC [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kila" with entities [EventEntity, EventEntity]
 60: 0x01F9 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=POWDER (ID: 17473707/0x010AA0AB), tag_num=0x04)
 61: 0x0200 [0x1C] WAIT(30* ticks)
 62: 0x0203 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kili" with entities [EventEntity, EventEntity]
 63: 0x0210 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "haed" with entities [EventEntity, EventEntity]
 64: 0x021D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kily" with entities [EventEntity, EventEntity]
 65: 0x022A [0x21] END_EVENT
 66: 0x022B [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                      2D F8 FF FF              -...
0230: 7F F8 FF FF 7F 6B 72 6F  69 00                    .....kroi.      
```

#### Opcodes

```
  0: 0x022C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kroi" with entities [EventEntity, EventEntity]
  1: 0x0239 [0x00] END_REQSTACK()
```

### Event 44

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x023A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                00                           .     
```

#### Opcodes

```
  0: 0x023A [0x00] END_REQSTACK()
```

### Event 45

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x023B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                   2D F8 FF FF 7F             -....
0240: F8 FF FF 7F 6B 69 6B 61  00                       ....kika.       
```

#### Opcodes

```
  0: 0x023B [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kika" with entities [EventEntity, EventEntity]
  1: 0x0248 [0x00] END_REQSTACK()
```

### Event 46

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0249   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                             2D F8 FF FF 7F F8 FF           -......
0250: FF 7F 6B 69 6B 62 00                              ..kikb.         
```

#### Opcodes

```
  0: 0x0249 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kikb" with entities [EventEntity, EventEntity]
  1: 0x0256 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0257  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                      00                                  .        
```

#### Opcodes

```
  0: 0x0257 [0x00] END_REQSTACK()
```

### Event 48

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0258   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                          2D F8 FF FF 7F F8 FF FF          -.......
0260: 7F 79 6F 6D 69 00                                 .yomi.          
```

#### Opcodes

```
  0: 0x0258 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "yomi" with entities [EventEntity, EventEntity]
  1: 0x0265 [0x00] END_REQSTACK()
```

### Event 49

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0266  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                   00                                    .         
```

#### Opcodes

```
  0: 0x0266 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0267  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                      00                                  .        
```

#### Opcodes

```
  0: 0x0267 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0268  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                          00                               .       
```

#### Opcodes

```
  0: 0x0268 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0269  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                             00                             .      
```

#### Opcodes

```
  0: 0x0269 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x026A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                                00                           .     
```

#### Opcodes

```
  0: 0x026A [0x00] END_REQSTACK()
```
