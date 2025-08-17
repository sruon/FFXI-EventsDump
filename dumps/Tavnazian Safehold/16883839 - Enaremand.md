# 16883839 - Enaremand

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 636 bytes                   |
| Total Events     | 17                          |
| References Count | 31                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [533](#event-533)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     17 |              5 |
| [534](#event-534)        | 0x0013       |      1 |              1 |
| [65535.2](#event-655352) | 0x0014       |     17 |              5 |
| [535](#event-535)        | 0x0025       |      1 |              1 |
| [65535.3](#event-655353) | 0x0026       |     10 |              2 |
| [65535.4](#event-655354) | 0x0030       |     24 |              6 |
| [65535.5](#event-655355) | 0x0048       |     14 |              4 |
| [536](#event-536)        | 0x0056       |      1 |              1 |
| [537](#event-537)        | 0x0057       |     36 |             10 |
| [538](#event-538)        | 0x007B       |     51 |             11 |
| [539](#event-539)        | 0x00AE       |     51 |             11 |
| [540](#event-540)        | 0x00E1       |     33 |              9 |
| [541](#event-541)        | 0x0102       |     48 |             10 |
| [65535.6](#event-655356) | 0x0132       |     86 |             16 |
| [542](#event-542)        | 0x0188       |     33 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x178A8     |       96424 |
|       2 | 0xD055      |       53333 |
|       3 | 0xFFFF5FD8  |  4294926296 |
|       4 | 0x00C8      |         200 |
|       5 | 0x178C1     |       96449 |
|       6 | 0xD58E      |       54670 |
|       7 | 0x1768D     |       95885 |
|       8 | 0xC984      |       51588 |
|       9 | 0xFFFF5FD0  |  4294926288 |
|      10 | 0x0D64      |        3428 |
|      11 | 0x003C      |          60 |
|      12 | 0x176CB     |       95947 |
|      13 | 0xCFCC      |       53196 |
|      14 | 0x0D5F      |        3423 |
|      15 | 0x17736     |       96054 |
|      16 | 0xC9E8      |       51688 |
|      17 | 0x001E      |          30 |
|      18 | 0x2B81      |       11137 |
|      19 | 0x0015      |          21 |
|      20 | 0x2B82      |       11138 |
|      21 | 0x0014      |          20 |
|      22 | 0x2B83      |       11139 |
|      23 | 0x001B      |          27 |
|      24 | 0x2B85      |       11141 |
|      25 | 0x2B86      |       11142 |
|      26 | 0x2B84      |       11140 |
|      27 | 0x0030      |          48 |
|      28 | 0x2B87      |       11143 |
|      29 | 0x2B88      |       11144 |
|      30 | 0x00F0      |         240 |

## String References

- **11137**: Only in a p-place like this c-can a m-m-m-man like m-m-m-me hide from the ridicule of the w-world.
- **11138**: Hm? Oh...um... Yes... Pay n-no heed t-to m-m-m-y ramblings...
- **11139**: I thought that in a p-place like this, I m-m-m-might be able to hide from the r-ridicule of the w-world. However, n-now that Tavnazia has reopened its doors to the outside...
- **11140**: B-but... You understand...r-right? No?
- **11141**: I never really needed a mannequin to remind me how beautiful my Alsha was...is.
- **11142**: That's right. From now on, she'll be here, right by my side...
- **11143**: Are you trying to tell me you have lost...?
- **11144**: Here. You must learn to cherish them with all you heart.

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

### Event 533

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1C    2.............
0010: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=96.424*, Z=53.333*, Y=-41.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1C] WAIT(200* ticks)
  4: 0x0012 [0x00] END_REQSTACK()
```

### Event 534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          00                                          .            
```

#### Opcodes

```
  0: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             32 00 80 1F  00 05 80 06 80 03 80 1F      2...........
0020: 01 1C 04 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0014 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0017 [0x1F] MOVE_ENTITY: EventEntity moves to X=96.449*, Z=54.670*, Y=-41.000*
  2: 0x001F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0021 [0x1C] WAIT(200* ticks)
  4: 0x0024 [0x00] END_REQSTACK()
```

### Event 535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                00                                      .          
```

#### Opcodes

```
  0: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   37 07  80 08 80 09 80 0A 80 00        7.........
```

#### Opcodes

```
  0: 0x0026 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=95.885*, z=51.588*, y=-41.008*, direction=301.3°*
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 00 80 1C 0B 80 1F 00  0C 80 0D 80 03 80 1F 01  2...............
0040: 4B 7F A0 01 01 0E 80 00                           K.......        
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0033 [0x1C] WAIT(60* ticks)
  2: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=95.947*, Z=53.196*, Y=-41.000*
  3: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0040 [0x4B] UPDATE_ENTITY_YAW(entity=Enaremand (ID: 16883839/0x0101A07F), yaw=18.8°*)
  5: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          32 00 80 1F 00 0F 80 10          2.......
0050: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0048 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=96.054*, Z=51.688*, Y=-41.000*
  2: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0055 [0x00] END_REQSTACK()
```

### Event 536

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0056  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   00                                    .         
```

#### Opcodes

```
  0: 0x0056 [0x00] END_REQSTACK()
```

### Event 537

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1E  F0 FF FF 7F 1C 11 80 1D         .........
0060: 12 80 23 66 13 80 7F A0  01 01 7F A0 01 01 64 69  ..#f..........di
0070: 73 30 1D 14 80 23 1C 11  80 21 00                 s0...#...!.     
```

#### Opcodes

```
  0: 0x0057 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005C [0x1C] WAIT(30* ticks)
  2: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=11137*)
    → "Only in a p-place like this c-can a m-m-m-man like m-m-m-me hide from the ridicule of the w-world."
  3: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=21*
  5: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=11138*)
    → "Hm? Oh...um... Yes... Pay n-no heed t-to m-m-m-y ramblings..."
  6: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0076 [0x1C] WAIT(30* ticks)
  8: 0x0079 [0x21] END_EVENT
  9: 0x007A [0x00] END_REQSTACK()
```

### Event 538

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 51 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   1E F0 FF FF 7F             .....
0080: 1C 11 80 66 15 80 7F A0  01 01 7F A0 01 01 74 68  ...f..........th
0090: 6B 31 1D 16 80 23 1D 14  80 23 66 15 80 7F A0 01  k1...#...#f.....
00A0: 01 7F A0 01 01 74 68 6B  32 1C 11 80 21 00        .....thk2...!.  
```

#### Opcodes

```
  0: 0x007B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0080 [0x1C] WAIT(30* ticks)
  2: 0x0083 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=20*
  3: 0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=11139*)
    → "I thought that in a p-place like this, I m-m-m-might be able to hide from the r-ridicule of the w-world. However, n-now that Tavnazia has reopened its doors to the outside..."
  4: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0096 [0x1D] PRINT_EVENT_MESSAGE(message_id=11138*)
    → "Hm? Oh...um... Yes... Pay n-no heed t-to m-m-m-y ramblings..."
  6: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x009A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=20*
  8: 0x00A9 [0x1C] WAIT(30* ticks)
  9: 0x00AC [0x21] END_EVENT
 10: 0x00AD [0x00] END_REQSTACK()
```

### Event 539

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 51 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            1E F0                ..
00B0: FF FF 7F 1C 11 80 66 17  80 7F A0 01 01 7F A0 01  ......f.........
00C0: 01 74 6C 62 30 1D 18 80  23 1D 19 80 23 66 17 80  .tlb0...#...#f..
00D0: 7F A0 01 01 7F A0 01 01  74 6C 62 31 1C 0B 80 21  ........tlb1...!
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AE [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B3 [0x1C] WAIT(30* ticks)
  2: 0x00B6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=27*
  3: 0x00C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=11141*)
    → "I never really needed a mannequin to remind me how beautiful my Alsha was...is."
  4: 0x00C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00C9 [0x1D] PRINT_EVENT_MESSAGE(message_id=11142*)
    → "That's right. From now on, she'll be here, right by my side..."
  6: 0x00CC [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00CD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=27*
  8: 0x00DC [0x1C] WAIT(60* ticks)
  9: 0x00DF [0x21] END_EVENT
 10: 0x00E0 [0x00] END_REQSTACK()
```

### Event 540

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    1E F0 FF FF 7F 1D 12  80 23 66 13 80 7F A0 01   ........#f.....
00F0: 01 7F A0 01 01 64 69 73  30 1D 1A 80 23 1C 11 80  .....dis0...#...
0100: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00E1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00E6 [0x1D] PRINT_EVENT_MESSAGE(message_id=11137*)
    → "Only in a p-place like this c-can a m-m-m-man like m-m-m-me hide from the ridicule of the w-world."
  2: 0x00E9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00EA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=21*
  4: 0x00F9 [0x1D] PRINT_EVENT_MESSAGE(message_id=11140*)
    → "B-but... You understand...r-right? No?"
  5: 0x00FC [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00FD [0x1C] WAIT(30* ticks)
  7: 0x0100 [0x21] END_EVENT
  8: 0x0101 [0x00] END_REQSTACK()
```

### Event 541

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 48 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       1E F0 FF FF 7F 66  15 80 7F A0 01 01 7F A0    .....f........
0110: 01 01 74 68 6B 31 1D 16  80 23 1D 1A 80 23 66 15  ..thk1...#...#f.
0120: 80 7F A0 01 01 7F A0 01  01 74 68 6B 32 1C 11 80  .........thk2...
0130: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0102 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0107 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=20*
  2: 0x0116 [0x1D] PRINT_EVENT_MESSAGE(message_id=11139*)
    → "I thought that in a p-place like this, I m-m-m-might be able to hide from the r-ridicule of the w-world. However, n-now that Tavnazia has reopened its doors to the outside..."
  3: 0x0119 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x011A [0x1D] PRINT_EVENT_MESSAGE(message_id=11140*)
    → "B-but... You understand...r-right? No?"
  5: 0x011D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x011E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=20*
  7: 0x012D [0x1C] WAIT(30* ticks)
  8: 0x0130 [0x21] END_EVENT
  9: 0x0131 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0132   |
| Data Size    | 86 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:       6E 85 A0 01 01 1B  80 99 85 A0 01 01 99 85    n.............
0140: A0 01 01 6E 81 A0 01 01  1B 80 99 81 A0 01 01 99  ...n............
0150: 81 A0 01 01 6E 82 A0 01  01 1B 80 99 82 A0 01 01  ....n...........
0160: 99 82 A0 01 01 6E 83 A0  01 01 1B 80 99 83 A0 01  .....n..........
0170: 01 99 83 A0 01 01 6E 84  A0 01 01 1B 80 99 84 A0  ......n.........
0180: 01 01 99 84 A0 01 01 00                           ........        
```

#### Opcodes

```
  0: 0x0132 [0x6E] manequin1 (ID: 16883845/0x0101A085) uses emote 48*
  1: 0x0139 [0x99] Wait for manequin1 (ID: 16883845/0x0101A085) animation to complete
  2: 0x013E [0x99] Wait for manequin1 (ID: 16883845/0x0101A085) animation to complete
  3: 0x0143 [0x6E] manequin2 (ID: 16883841/0x0101A081) uses emote 48*
  4: 0x014A [0x99] Wait for manequin2 (ID: 16883841/0x0101A081) animation to complete
  5: 0x014F [0x99] Wait for manequin2 (ID: 16883841/0x0101A081) animation to complete
  6: 0x0154 [0x6E] manequin3 (ID: 16883842/0x0101A082) uses emote 48*
  7: 0x015B [0x99] Wait for manequin3 (ID: 16883842/0x0101A082) animation to complete
  8: 0x0160 [0x99] Wait for manequin3 (ID: 16883842/0x0101A082) animation to complete
  9: 0x0165 [0x6E] manequin4 (ID: 16883843/0x0101A083) uses emote 48*
 10: 0x016C [0x99] Wait for manequin4 (ID: 16883843/0x0101A083) animation to complete
 11: 0x0171 [0x99] Wait for manequin4 (ID: 16883843/0x0101A083) animation to complete
 12: 0x0176 [0x6E] manequin5 (ID: 16883844/0x0101A084) uses emote 48*
 13: 0x017D [0x99] Wait for manequin5 (ID: 16883844/0x0101A084) animation to complete
 14: 0x0182 [0x99] Wait for manequin5 (ID: 16883844/0x0101A084) animation to complete
 15: 0x0187 [0x00] END_REQSTACK()
```

### Event 542

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0188   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                          1E F0 FF FF 7F 1D 1C 80          ........
0190: 23 1D 1D 80 23 66 15 80  7F A0 01 01 7F A0 01 01  #...#f..........
01A0: 70 61 73 30 1C 1E 80 21  00                       pas0...!.       
```

#### Opcodes

```
  0: 0x0188 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x018D [0x1D] PRINT_EVENT_MESSAGE(message_id=11143*)
    → "Are you trying to tell me you have lost...?"
  2: 0x0190 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0191 [0x1D] PRINT_EVENT_MESSAGE(message_id=11144*)
    → "Here. You must learn to cherish them with all you heart."
  4: 0x0194 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0195 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [Enaremand (ID: 16883839/0x0101A07F), Enaremand (ID: 16883839/0x0101A07F)], work=20*
  6: 0x01A4 [0x1C] WAIT(240* ticks)
  7: 0x01A7 [0x21] END_EVENT
  8: 0x01A8 [0x00] END_REQSTACK()
```
