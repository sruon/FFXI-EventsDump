# 17162909 - Karaha-Baruha

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 592 bytes                    |
| Total Events     | 12                           |
| References Count | 18                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [234](#event-234)        | 0x0001       |      1 |              1 |
| [186](#event-186)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     21 |              5 |
| [23](#event-23)          | 0x0018       |      1 |              1 |
| [24](#event-24)          | 0x0019       |      1 |              1 |
| [65535.2](#event-655352) | 0x001A       |     14 |              4 |
| [65535.3](#event-655353) | 0x0028       |    196 |             22 |
| [65535.4](#event-655354) | 0x00EC       |    164 |             20 |
| [65535.5](#event-655355) | 0x0190       |     11 |              3 |
| [65535.6](#event-655356) | 0x019B       |     19 |              5 |
| [65535.7](#event-655357) | 0x01AE       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0B98      |        2968 |
|       1 | 0x45AE      |       17838 |
|       2 | 0xFFFF9A71  |  4294941297 |
|       3 | 0x000A      |          10 |
|       4 | 0xFFFFEEDD  |  4294962909 |
|       5 | 0xFFFFE444  |  4294960196 |
|       6 | 0xFFFF9C65  |  4294941797 |
|       7 | 0x01F8      |         504 |
|       8 | 0x0000      |           0 |
|       9 | 0xFFFFE321  |  4294959905 |
|      10 | 0xFFFFDCDB  |  4294958299 |
|      11 | 0x1EE3      |        7907 |
|      12 | 0x0A4A      |        2634 |
|      13 | 0x0FC2      |        4034 |
|      14 | 0x054E      |        1358 |
|      15 | 0x2F7E      |       12158 |
|      16 | 0x4391      |       17297 |
|      17 | 0xFFFF9976  |  4294941046 |

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

### Event 234

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

### Event 186

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          1F 00 00 80 01  80 02 80 1F 01 6F 4A 9D     ..........oJ.
0010: E2 05 01 18 E2 05 01 00                           ........        
```

#### Opcodes

```
  0: 0x0003 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.968*, Z=17.838*, Y=-25.999*
  1: 0x000B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x000D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000E [0x4A] Karaha-Baruha (ID: 17162909/0x0105E29D) looks at Robel-Akbel (ID: 17162776/0x0105E218)
  4: 0x0017 [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          00                               .       
```

#### Opcodes

```
  0: 0x0018 [0x00] END_REQSTACK()
```

### Event 24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             00                             .      
```

#### Opcodes

```
  0: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 03 80 1F 00 04            2.....
0020: 80 05 80 06 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-4.387*, Z=-7.100*, Y=-25.499*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0028    |
| Data Size    | 196 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1F 00 04 80 05 80 06 80          ........
0030: 1F 01 4A F0 FF FF 7F 9D  E2 05 01 4A 08 E2 05 01  ..J........J....
0040: 9D E2 05 01 4A 07 E2 05  01 9D E2 05 01 4A 0C E2  ....J........J..
0050: 05 01 9D E2 05 01 4A 0E  E2 05 01 9D E2 05 01 4A  ......J........J
0060: 0F E2 05 01 9D E2 05 01  4A 11 E2 05 01 9D E2 05  ........J.......
0070: 01 4A 12 E2 05 01 9D E2  05 01 4A 10 E2 05 01 9D  .J........J.....
0080: E2 05 01 4A 13 E2 05 01  9D E2 05 01 4A 2C E2 05  ...J........J,..
0090: 01 9D E2 05 01 4A 2D E2  05 01 9D E2 05 01 4A 2E  .....J-.......J.
00A0: E2 05 01 9D E2 05 01 4A  2F E2 05 01 9D E2 05 01  .......J/.......
00B0: 4A 30 E2 05 01 9D E2 05  01 4A 31 E2 05 01 9D E2  J0.......J1.....
00C0: 05 01 4A 32 E2 05 01 9D  E2 05 01 52 07 80 F0 FF  ..J2.......R....
00D0: FF 7F F0 FF FF 7F 30 34  30 74 45 07 80 F0 FF FF  ......040tE.....
00E0: 7F F0 FF FF 7F 30 34 30  75 08 80 00              .....040u...    
```

#### Opcodes

```
  0: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=-4.387*, Z=-7.100*, Y=-25.499*
  1: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0032 [0x4A] LocalPlayer looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  3: 0x003B [0x4A] Romaa Mihgo (ID: 17162760/0x0105E208) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  4: 0x0044 [0x4A] Perih Vashai (ID: 17162759/0x0105E207) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  5: 0x004D [0x4A] Haja Zhwan (ID: 17162764/0x0105E20C) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  6: 0x0056 [0x4A] Mikhe Aryohcha (ID: 17162766/0x0105E20E) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  7: 0x005F [0x4A] Vhino Delkahngo (ID: 17162767/0x0105E20F) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  8: 0x0068 [0x4A] Naho Gwanboh (ID: 17162769/0x0105E211) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  9: 0x0071 [0x4A] Nzha Abaleenah (ID: 17162770/0x0105E212) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 10: 0x007A [0x4A] Lhu Mhakaracca (ID: 17162768/0x0105E210) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 11: 0x0083 [0x4A] Ghyo Molkot (ID: 17162771/0x0105E213) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 12: 0x008C [0x4A] Zolku-Azolku (ID: 17162796/0x0105E22C) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 13: 0x0095 [0x4A] Kayeel-Payeel (ID: 17162797/0x0105E22D) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 14: 0x009E [0x4A] Lutete (ID: 17162798/0x0105E22E) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 15: 0x00A7 [0x4A] Gariri (ID: 17162799/0x0105E22F) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 16: 0x00B0 [0x4A] Zonpa-Zippa (ID: 17162800/0x0105E230) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 17: 0x00B9 [0x4A] Zubaba (ID: 17162801/0x0105E231) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 18: 0x00C2 [0x4A] Pattna-Ottna (ID: 17162802/0x0105E232) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 19: 0x00CB [0x52] END_LOAD_SCHEDULER: End scheduler "040t" with entities [LocalPlayer, LocalPlayer], work=504*
 20: 0x00DA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "040u" with entities [LocalPlayer, LocalPlayer], work=[504*, 0*]
 21: 0x00EB [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00EC    |
| Data Size    | 164 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      1F 00 09 80              ....
00F0: 0A 80 06 80 1F 01 4A F0  FF FF 7F 9D E2 05 01 4A  ......J........J
0100: 08 E2 05 01 9D E2 05 01  4A 07 E2 05 01 9D E2 05  ........J.......
0110: 01 4A 0C E2 05 01 9D E2  05 01 4A 0E E2 05 01 9D  .J........J.....
0120: E2 05 01 4A 0F E2 05 01  9D E2 05 01 4A 11 E2 05  ...J........J...
0130: 01 9D E2 05 01 4A 12 E2  05 01 9D E2 05 01 4A 10  .....J........J.
0140: E2 05 01 9D E2 05 01 4A  13 E2 05 01 9D E2 05 01  .......J........
0150: 4A 2C E2 05 01 9D E2 05  01 4A 2D E2 05 01 9D E2  J,.......J-.....
0160: 05 01 4A 2E E2 05 01 9D  E2 05 01 4A 2F E2 05 01  ..J........J/...
0170: 9D E2 05 01 4A 30 E2 05  01 9D E2 05 01 4A 31 E2  ....J0.......J1.
0180: 05 01 9D E2 05 01 4A 32  E2 05 01 9D E2 05 01 00  ......J2........
```

#### Opcodes

```
  0: 0x00EC [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.391*, Z=-8.997*, Y=-25.499*
  1: 0x00F4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00F6 [0x4A] LocalPlayer looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  3: 0x00FF [0x4A] Romaa Mihgo (ID: 17162760/0x0105E208) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  4: 0x0108 [0x4A] Perih Vashai (ID: 17162759/0x0105E207) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  5: 0x0111 [0x4A] Haja Zhwan (ID: 17162764/0x0105E20C) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  6: 0x011A [0x4A] Mikhe Aryohcha (ID: 17162766/0x0105E20E) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  7: 0x0123 [0x4A] Vhino Delkahngo (ID: 17162767/0x0105E20F) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  8: 0x012C [0x4A] Naho Gwanboh (ID: 17162769/0x0105E211) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
  9: 0x0135 [0x4A] Nzha Abaleenah (ID: 17162770/0x0105E212) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 10: 0x013E [0x4A] Lhu Mhakaracca (ID: 17162768/0x0105E210) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 11: 0x0147 [0x4A] Ghyo Molkot (ID: 17162771/0x0105E213) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 12: 0x0150 [0x4A] Zolku-Azolku (ID: 17162796/0x0105E22C) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 13: 0x0159 [0x4A] Kayeel-Payeel (ID: 17162797/0x0105E22D) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 14: 0x0162 [0x4A] Lutete (ID: 17162798/0x0105E22E) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 15: 0x016B [0x4A] Gariri (ID: 17162799/0x0105E22F) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 16: 0x0174 [0x4A] Zonpa-Zippa (ID: 17162800/0x0105E230) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 17: 0x017D [0x4A] Zubaba (ID: 17162801/0x0105E231) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 18: 0x0186 [0x4A] Pattna-Ottna (ID: 17162802/0x0105E232) looks at Karaha-Baruha (ID: 17162909/0x0105E29D)
 19: 0x018F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0190   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190: 1F 00 0B 80 0C 80 06 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0190 [0x1F] MOVE_ENTITY: EventEntity moves to X=7.907*, Z=2.634*, Y=-25.499*
  1: 0x0198 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x019A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019B   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                   32 03 80 1F 00             2....
01A0: 0D 80 0E 80 06 80 1F 01  1E 18 E2 05 01 00        ..............  
```

#### Opcodes

```
  0: 0x019B [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x019E [0x1F] MOVE_ENTITY: EventEntity moves to X=4.034*, Z=1.358*, Y=-25.499*
  2: 0x01A6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01A8 [0x1E] EventEntity looks at Robel-Akbel (ID: 17162776/0x0105E218) and starts talking
  4: 0x01AD [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AE   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                            32 03                2.
01B0: 80 1F 00 0F 80 10 80 11  80 1F 01 1E 18 E2 05 01  ................
01C0: 7B 9D E2 05 01 00                                 {.....          
```

#### Opcodes

```
  0: 0x01AE [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x01B1 [0x1F] MOVE_ENTITY: EventEntity moves to X=12.158*, Z=17.297*, Y=-26.250*
  2: 0x01B9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01BB [0x1E] EventEntity looks at Robel-Akbel (ID: 17162776/0x0105E218) and starts talking
  4: 0x01C0 [0x7B] Karaha-Baruha (ID: 17162909/0x0105E29D) stops talking
  5: 0x01C5 [0x00] END_REQSTACK()
```
