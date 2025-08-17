# 17162725 - Chioh Remhrll

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 668 bytes                    |
| Total Events     | 11                           |
| References Count | 51                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [413](#event-413)        | 0x0000       |     60 |             10 |
| [231](#event-231)        | 0x003C       |      1 |              1 |
| [163](#event-163)        | 0x003D       |     73 |             13 |
| [32](#event-32)          | 0x0086       |      1 |              1 |
| [65535](#event-65535)    | 0x0087       |    110 |             23 |
| [65535.1](#event-655351) | 0x00F5       |     31 |              8 |
| [65535.2](#event-655352) | 0x0114       |     50 |             11 |
| [65535.3](#event-655353) | 0x0146       |     20 |              5 |
| [65535.4](#event-655354) | 0x015A       |     29 |              6 |
| [65535.5](#event-655355) | 0x0177       |     29 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x003B      |          59 |
|       2 | 0x2AA1      |       10913 |
|       3 | 0x2AA2      |       10914 |
|       4 | 0x1492      |        5266 |
|       5 | 0x2B57      |       11095 |
|       6 | 0x2B58      |       11096 |
|       7 | 0x2B59      |       11097 |
|       8 | 0x0028      |          40 |
|       9 | 0x042C      |        1068 |
|      10 | 0x52A8      |       21160 |
|      11 | 0xFFFFFC19  |  4294966297 |
|      12 | 0xFFFFFFBF  |  4294967231 |
|      13 | 0x5BED      |       23533 |
|      14 | 0xFFFFF79B  |  4294965147 |
|      15 | 0x65C2      |       26050 |
|      16 | 0xFFFFE8CE  |  4294961358 |
|      17 | 0x77A7      |       30631 |
|      18 | 0xFFFFD3A3  |  4294955939 |
|      19 | 0x85F8      |       34296 |
|      20 | 0xFFFFB5DC  |  4294948316 |
|      21 | 0x8EEE      |       36590 |
|      22 | 0xFFFFF7A6  |  4294965158 |
|      23 | 0xFFFF906F  |  4294938735 |
|      24 | 0x9972      |       39282 |
|      25 | 0xFFFFF255  |  4294963797 |
|      26 | 0xFFFF7216  |  4294930966 |
|      27 | 0xA127      |       41255 |
|      28 | 0xFFFF4523  |  4294919459 |
|      29 | 0xA881      |       43137 |
|      30 | 0xFFFFF254  |  4294963796 |
|      31 | 0xFFFF3A2B  |  4294916651 |
|      32 | 0xAE4A      |       44618 |
|      33 | 0xFFFF3A94  |  4294916756 |
|      34 | 0xAFCE      |       45006 |
|      35 | 0x000D      |          13 |
|      36 | 0xFFFF33D7  |  4294915031 |
|      37 | 0xAA40      |       43584 |
|      38 | 0xFFFF3018  |  4294914072 |
|      39 | 0xB54A      |       46410 |
|      40 | 0xFFFF3742  |  4294915906 |
|      41 | 0xC242      |       49730 |
|      42 | 0xFFFF3A26  |  4294916646 |
|      43 | 0xCAD0      |       51920 |
|      44 | 0xFFFF3707  |  4294915847 |
|      45 | 0xB608      |       46600 |
|      46 | 0x07C1      |        1985 |
|      47 | 0x3895      |       14485 |
|      48 | 0xFFFFFC18  |  4294966296 |
|      49 | 0x0398      |         920 |
|      50 | 0x36CB      |       14027 |

## Events

### Event 413

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 4A F8 FF FF 7F F0 FF FF  7F 1C 00 80 66 01 80 F8  J...........f...
0010: FF FF 7F F8 FF FF 7F 74  6C 6B 30 2B F8 FF FF 7F  .......tlk0+....
0020: 02 80 23 2B F8 FF FF 7F  03 80 23 66 01 80 F8 FF  ..#+......#f....
0030: FF 7F F8 FF FF 7F 74 6C  6B 31 21 00              ......tlk1!.    
```

#### Opcodes

```
  0: 0x0000 [0x4A] EventEntity looks at LocalPlayer
  1: 0x0009 [0x1C] WAIT(30* ticks)
  2: 0x000C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x001B [0x2B] EventEntity [10913*]:
    → "This is the Huntsman's Court. For generations now it has been a gathering place for Mithran rangers to sell their catches."
  4: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0023 [0x2B] EventEntity [10914*]:
    → "But now it has become a makeshift barracks for the Mithra Mercenaries."
  6: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  8: 0x003A [0x21] END_EVENT
  9: 0x003B [0x00] END_REQSTACK()
```

### Event 231

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```

### Event 163

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 73 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         4A F8 FF               J..
0040: FF 7F F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F  .........f......
0050: F8 FF FF 7F 74 6C 6B 30  03 02 10 04 80 2B F8 FF  ....tlk0.....+..
0060: FF 7F 05 80 23 2B F8 FF  FF 7F 06 80 23 2B F8 FF  ....#+......#+..
0070: FF 7F 07 80 23 66 01 80  F8 FF FF 7F F8 FF FF 7F  ....#f..........
0080: 74 6C 6B 31 21 00                                 tlk1!.          
```

#### Opcodes

```
  0: 0x003D [0x4A] EventEntity looks at LocalPlayer
  1: 0x0046 [0x1C] WAIT(30* ticks)
  2: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x0058 [0x03] Work_Zone[2] = 5266*
  4: 0x005D [0x2B] EventEntity [11095*]:
    → "We Mithra, rrregardless of upbringing, have one thing in common: We're all suckers for $0! So the choice is obvious!"
  5: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0065 [0x2B] EventEntity [11096*]:
    → "It's just that I haven't seen any since coming over to this continent. And it could be prrricey to import..."
  7: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x006D [0x2B] EventEntity [11097*]:
    → "But when I recall the overwhelming sensation of ecstasy you get from just a whiff...I'm convinced it's worth the cost. No other food has such a ferrrocious hold over us Mithra!"
  9: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0075 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 11: 0x0084 [0x21] END_EVENT
 12: 0x0085 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   00                                    .         
```

#### Opcodes

```
  0: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0087    |
| Data Size    | 110 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      59  04 F8 FF FF 7F 08 80 1F         Y........
0090: 00 09 80 0A 80 0B 80 1F  01 1F 00 0C 80 0D 80 0B  ................
00A0: 80 1F 01 1F 00 0E 80 0F  80 0B 80 1F 01 1F 00 10  ................
00B0: 80 11 80 0B 80 1F 01 1F  00 12 80 13 80 0B 80 1F  ................
00C0: 01 1F 00 14 80 15 80 16  80 1F 01 1F 00 17 80 18  ................
00D0: 80 19 80 1F 01 1F 00 1A  80 1B 80 19 80 1F 01 1F  ................
00E0: 00 1C 80 1D 80 1E 80 1F  01 1F 00 1F 80 20 80 1E  ............. ..
00F0: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0087 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 40* * 0.1
  1: 0x008F [0x1F] MOVE_ENTITY: EventEntity moves to X=1.068*, Z=21.160*, Y=-0.999*
  2: 0x0097 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0099 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.065*, Z=23.533*, Y=-0.999*
  4: 0x00A1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00A3 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.149*, Z=26.050*, Y=-0.999*
  6: 0x00AB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=-5.938*, Z=30.631*, Y=-0.999*
  8: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00B7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-11.357*, Z=34.296*, Y=-0.999*
 10: 0x00BF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x00C1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.980*, Z=36.590*, Y=-2.138*
 12: 0x00C9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x00CB [0x1F] MOVE_ENTITY: EventEntity moves to X=-28.561*, Z=39.282*, Y=-3.499*
 14: 0x00D3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x00D5 [0x1F] MOVE_ENTITY: EventEntity moves to X=-36.330*, Z=41.255*, Y=-3.499*
 16: 0x00DD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 17: 0x00DF [0x1F] MOVE_ENTITY: EventEntity moves to X=-47.837*, Z=43.137*, Y=-3.500*
 18: 0x00E7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 19: 0x00E9 [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.645*, Z=44.618*, Y=-3.500*
 20: 0x00F1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 21: 0x00F3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 22: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 31 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                59 04 F8  FF FF 7F 08 80 1F 00 1F       Y..........
0100: 80 20 80 1E 80 1F 01 6F  1F 00 21 80 22 80 19 80  . .....o..!."...
0110: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x00F5 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 40* * 0.1
  1: 0x00FD [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.645*, Z=44.618*, Y=-3.500*
  2: 0x0105 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0107 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0108 [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.540*, Z=45.006*, Y=-3.499*
  5: 0x0110 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0112 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 50 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             59 04 F8 FF  FF 7F 23 80 1F 00 24 80      Y.....#...$.
0120: 25 80 19 80 1F 01 1F 00  26 80 27 80 19 80 1F 01  %.......&.'.....
0130: 1F 00 28 80 29 80 19 80  1F 01 1F 00 2A 80 2B 80  ..(.).......*.+.
0140: 19 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0114 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x011C [0x1F] MOVE_ENTITY: EventEntity moves to X=-52.265*, Z=43.584*, Y=-3.499*
  2: 0x0124 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0126 [0x1F] MOVE_ENTITY: EventEntity moves to X=-53.224*, Z=46.410*, Y=-3.499*
  4: 0x012E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0130 [0x1F] MOVE_ENTITY: EventEntity moves to X=-51.390*, Z=49.730*, Y=-3.499*
  6: 0x0138 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x013A [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.650*, Z=51.920*, Y=-3.499*
  8: 0x0142 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0144 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x0145 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0146   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   59 04  F8 FF FF 7F 23 80 1F 00        Y.....#...
0150: 2C 80 2D 80 1E 80 1F 01  6F 00                    ,.-.....o.      
```

#### Opcodes

```
  0: 0x0146 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x014E [0x1F] MOVE_ENTITY: EventEntity moves to X=-51.449*, Z=46.600*, Y=-3.500*
  2: 0x0156 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0158 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0159 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015A   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                59 04 F8 FF FF 7F            Y.....
0160: 08 80 1F 00 2E 80 2F 80  30 80 1F 01 6F 4A F8 FF  ....../.0...oJ..
0170: FF 7F FF E1 05 01 00                              .......         
```

#### Opcodes

```
  0: 0x015A [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 40* * 0.1
  1: 0x0162 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.985*, Z=14.485*, Y=-1.000*
  2: 0x016A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x016C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x016D [0x4A] EventEntity looks at Dhea Prandoleh (ID: 17162751/0x0105E1FF)
  5: 0x0176 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0177   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                      59  04 F8 FF FF 7F 08 80 1F         Y........
0180: 00 31 80 32 80 0B 80 1F  01 6F 4A F8 FF FF 7F FF  .1.2.....oJ.....
0190: E1 05 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0177 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 40* * 0.1
  1: 0x017F [0x1F] MOVE_ENTITY: EventEntity moves to X=0.920*, Z=14.027*, Y=-0.999*
  2: 0x0187 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0189 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x018A [0x4A] EventEntity looks at Dhea Prandoleh (ID: 17162751/0x0105E1FF)
  5: 0x0193 [0x00] END_REQSTACK()
```
