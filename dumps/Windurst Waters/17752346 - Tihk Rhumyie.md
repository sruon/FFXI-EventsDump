# 17752346 - Tihk Rhumyie

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 852 bytes                 |
| Total Events     | 11                        |
| References Count | 33                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [989](#event-989)        | 0x0001       |      1 |              1 |
| [1016](#event-1016)      | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |    279 |             41 |
| [65535.2](#event-655352) | 0x011A       |    121 |             21 |
| [65535.3](#event-655353) | 0x0193       |     24 |              6 |
| [65535.4](#event-655354) | 0x01AB       |    121 |             21 |
| [65535.5](#event-655355) | 0x0224       |     14 |              4 |
| [65535.6](#event-655356) | 0x0232       |     24 |              6 |
| [65535.7](#event-655357) | 0x024A       |     73 |             11 |
| [991](#event-991)        | 0x0293       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0013      |          19 |
|       1 | 0x261D      |        9757 |
|       2 | 0x53B1      |       21425 |
|       3 | 0xFFFFFC18  |  4294966296 |
|       4 | 0x00D6      |         214 |
|       5 | 0x02AF      |         687 |
|       6 | 0x690E      |       26894 |
|       7 | 0x092A      |        2346 |
|       8 | 0xFFFFE778  |  4294961016 |
|       9 | 0x737D      |       29565 |
|      10 | 0x0123      |         291 |
|      11 | 0xFFFFFF0E  |  4294967054 |
|      12 | 0x7261      |       29281 |
|      13 | 0xFFFFEAAC  |  4294961836 |
|      14 | 0x6BBC      |       27580 |
|      15 | 0x0986      |        2438 |
|      16 | 0xFFFFF2B7  |  4294963895 |
|      17 | 0x778C      |       30604 |
|      18 | 0xFFFFFC19  |  4294966297 |
|      19 | 0x0A20      |        2592 |
|      20 | 0x003C      |          60 |
|      21 | 0x2AF8      |       11000 |
|      22 | 0x5208      |       21000 |
|      23 | 0x052B      |        1323 |
|      24 | 0x001E      |          30 |
|      25 | 0x000B      |          11 |
|      26 | 0x2178      |        8568 |
|      27 | 0x5524      |       21796 |
|      28 | 0x000F      |          15 |
|      29 | 0x3AFB      |       15099 |
|      30 | 0x0000      |           0 |
|      31 | 0x0001      |           1 |
|      32 | 0x0078      |         120 |

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

### Event 989

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

### Event 1016

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

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0003    |
| Data Size    | 279 bytes |
| Instructions | 41        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          46 01 94 01 F0  FF FF 7F 92 01 19 E1 0E     F............
0010: 01 92 01 71 E0 0E 01 92  01 70 E0 0E 01 92 01 27  ...q.....p.....'
0020: E0 0E 01 92 01 72 E0 0E  01 94 01 19 E1 0E 01 38  .....r.........8
0030: 00 80 BA F0 FF FF 7F 01  80 02 80 03 80 04 80 BA  ................
0040: 1A E1 0E 01 05 80 06 80  03 80 07 80 BA 1B E1 0E  ................
0050: 01 08 80 09 80 03 80 0A  80 BA 1C E1 0E 01 0B 80  ................
0060: 0C 80 03 80 07 80 BA 1E  E1 0E 01 0D 80 0E 80 03  ................
0070: 80 0F 80 BA 1F E1 0E 01  10 80 11 80 12 80 13 80  ................
0080: 80 F0 FF FF 7F 80 19 E1  0E 01 80 1A E1 0E 01 80  ................
0090: 1B E1 0E 01 80 1C E1 0E  01 80 1E E1 0E 01 80 1F  ................
00A0: E1 0E 01 80 71 E0 0E 01  80 70 E0 0E 01 80 27 E0  ....q....p....'.
00B0: 0E 01 80 72 E0 0E 01 4A  19 E1 0E 01 1A E1 0E 01  ...r...J........
00C0: 6F 76 19 E1 0E 01 1C 14  80 3A 19 E1 0E 01 00 00  ov.......:......
00D0: BA 18 E1 0E 01 15 80 16  80 03 80 00 00 2F 00 18  ............./..
00E0: E1 0E 01 4E 00 18 E1 0E  01 92 01 18 E1 0E 01 94  ...N............
00F0: 01 18 E1 0E 01 80 18 E1  0E 01 5B 17 80 18 E1 0E  ..........[.....
0100: 01 18 E1 0E 01 68 6F 6E  30 53 18 E1 0E 01 18 E1  .....hon0S......
0110: 0E 01 68 6F 6E 30 1C 18  80 00                    ..hon0....      
```

#### Opcodes

```
  0: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x0005 [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  2: 0x000B [0x92] Khoto Rokkorah (ID: 17752345/0x010EE119)->Render.Flags3 ^= 0x01
  3: 0x0011 [0x92] Okaka (ID: 17752177/0x010EE071)->Render.Flags3 ^= 0x01
  4: 0x0017 [0x92] Miriri (ID: 17752176/0x010EE070)->Render.Flags3 ^= 0x01
  5: 0x001D [0x92] Ahyeekih (ID: 17752103/0x010EE027)->Render.Flags3 ^= 0x01
  6: 0x0023 [0x92] Damami-Karumi (ID: 17752178/0x010EE072)->Render.Flags3 ^= 0x01
  7: 0x0029 [0x94] Khoto Rokkorah (ID: 17752345/0x010EE119)->Render.Flags3 ^= 0x01
  8: 0x002F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  9: 0x0032 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=9.757*, pos_z=21.425*, pos_y=-1.000*, direction=18.8°*)
 10: 0x003F [0xBA] SET_ENTITY_POSITION(entity_id=Tihk Rhumyie (ID: 17752346/0x010EE11A), pos_x=0.687*, pos_z=26.894*, pos_y=-1.000*, direction=206.2°*)
 11: 0x004C [0xBA] SET_ENTITY_POSITION(entity_id=Kuppo-Pippo (ID: 17752347/0x010EE11B), pos_x=-6.280*, pos_z=29.565*, pos_y=-1.000*, direction=25.6°*)
 12: 0x0059 [0xBA] SET_ENTITY_POSITION(entity_id=Karanka-Tonka (ID: 17752348/0x010EE11C), pos_x=-0.242*, pos_z=29.281*, pos_y=-1.000*, direction=206.2°*)
 13: 0x0066 [0xBA] SET_ENTITY_POSITION(entity_id=Cotta-Lotta (ID: 17752350/0x010EE11E), pos_x=-5.460*, pos_z=27.580*, pos_y=-1.000*, direction=214.3°*)
 14: 0x0073 [0xBA] SET_ENTITY_POSITION(entity_id=Tacca-Picca (ID: 17752351/0x010EE11F), pos_x=-3.401*, pos_z=30.604*, pos_y=-0.999*, direction=227.8°*)
 15: 0x0080 [0x80] LOAD_WAIT(entity=LocalPlayer)
 16: 0x0085 [0x80] LOAD_WAIT(entity=Khoto Rokkorah (ID: 17752345/0x010EE119))
 17: 0x008A [0x80] LOAD_WAIT(entity=Tihk Rhumyie (ID: 17752346/0x010EE11A))
 18: 0x008F [0x80] LOAD_WAIT(entity=Kuppo-Pippo (ID: 17752347/0x010EE11B))
 19: 0x0094 [0x80] LOAD_WAIT(entity=Karanka-Tonka (ID: 17752348/0x010EE11C))
 20: 0x0099 [0x80] LOAD_WAIT(entity=Cotta-Lotta (ID: 17752350/0x010EE11E))
 21: 0x009E [0x80] LOAD_WAIT(entity=Tacca-Picca (ID: 17752351/0x010EE11F))
 22: 0x00A3 [0x80] LOAD_WAIT(entity=Okaka (ID: 17752177/0x010EE071))
 23: 0x00A8 [0x80] LOAD_WAIT(entity=Miriri (ID: 17752176/0x010EE070))
 24: 0x00AD [0x80] LOAD_WAIT(entity=Ahyeekih (ID: 17752103/0x010EE027))
 25: 0x00B2 [0x80] LOAD_WAIT(entity=Damami-Karumi (ID: 17752178/0x010EE072))
 26: 0x00B7 [0x4A] Khoto Rokkorah (ID: 17752345/0x010EE119) looks at Tihk Rhumyie (ID: 17752346/0x010EE11A)
 27: 0x00C0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 28: 0x00C1 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Khoto Rokkorah (ID: 17752345/0x010EE119) Render.Flags0 and Render.Flags3 conditions are met
 29: 0x00C6 [0x1C] WAIT(60* ticks)
 30: 0x00C9 [0x3A] CONVERT_YAW_TO_BYTE(entity=Khoto Rokkorah (ID: 17752345/0x010EE119), result_destination=ExtData[1]->WorkLocal[0])
 31: 0x00D0 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17752344/0x010EE118), pos_x=11.000*, pos_z=21.000*, pos_y=-1.000*, direction=ExtData[1]->WorkLocal[0])
 32: 0x00DD [0x2F] Unnamed NPC (ID: 17752344/0x010EE118)->Render.Flags0 &= ~0x80000 // Bit 19
 33: 0x00E3 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17752344/0x010EE118)
 34: 0x00E9 [0x92] Unnamed NPC (ID: 17752344/0x010EE118)->Render.Flags3 ^= 0x01
 35: 0x00EF [0x94] Unnamed NPC (ID: 17752344/0x010EE118)->Render.Flags3 ^= 0x01
 36: 0x00F5 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17752344/0x010EE118))
 37: 0x00FA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon0" with entities [Unnamed NPC (ID: 17752344/0x010EE118), Unnamed NPC (ID: 17752344/0x010EE118)], work=1323*
 38: 0x0109 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hon0" with entities [Unnamed NPC (ID: 17752344/0x010EE118), Unnamed NPC (ID: 17752344/0x010EE118)]
 39: 0x0116 [0x1C] WAIT(30* ticks)
 40: 0x0119 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x011A    |
| Data Size    | 121 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                2F 00 1A E1 0E 01            /.....
0120: 2F 00 1B E1 0E 01 2F 00  1C E1 0E 01 2F 00 1E E1  /...../...../...
0130: 0E 01 2F 00 1F E1 0E 01  4E 00 1A E1 0E 01 4E 00  ../.....N.....N.
0140: 1B E1 0E 01 4E 00 1C E1  0E 01 4E 00 1E E1 0E 01  ....N.....N.....
0150: 4E 00 1F E1 0E 01 92 01  1A E1 0E 01 92 01 1B E1  N...............
0160: 0E 01 92 01 1C E1 0E 01  92 01 1E E1 0E 01 92 01  ................
0170: 1F E1 0E 01 94 01 1A E1  0E 01 94 01 1B E1 0E 01  ................
0180: 94 01 1C E1 0E 01 94 01  1E E1 0E 01 94 01 1F E1  ................
0190: 0E 01 00                                          ...             
```

#### Opcodes

```
  0: 0x011A [0x2F] Tihk Rhumyie (ID: 17752346/0x010EE11A)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0120 [0x2F] Kuppo-Pippo (ID: 17752347/0x010EE11B)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0126 [0x2F] Karanka-Tonka (ID: 17752348/0x010EE11C)->Render.Flags0 &= ~0x80000 // Bit 19
  3: 0x012C [0x2F] Cotta-Lotta (ID: 17752350/0x010EE11E)->Render.Flags0 &= ~0x80000 // Bit 19
  4: 0x0132 [0x2F] Tacca-Picca (ID: 17752351/0x010EE11F)->Render.Flags0 &= ~0x80000 // Bit 19
  5: 0x0138 [0x4E] SET_ENTITY_HIDE_FLAG: Show Tihk Rhumyie (ID: 17752346/0x010EE11A)
  6: 0x013E [0x4E] SET_ENTITY_HIDE_FLAG: Show Kuppo-Pippo (ID: 17752347/0x010EE11B)
  7: 0x0144 [0x4E] SET_ENTITY_HIDE_FLAG: Show Karanka-Tonka (ID: 17752348/0x010EE11C)
  8: 0x014A [0x4E] SET_ENTITY_HIDE_FLAG: Show Cotta-Lotta (ID: 17752350/0x010EE11E)
  9: 0x0150 [0x4E] SET_ENTITY_HIDE_FLAG: Show Tacca-Picca (ID: 17752351/0x010EE11F)
 10: 0x0156 [0x92] Tihk Rhumyie (ID: 17752346/0x010EE11A)->Render.Flags3 ^= 0x01
 11: 0x015C [0x92] Kuppo-Pippo (ID: 17752347/0x010EE11B)->Render.Flags3 ^= 0x01
 12: 0x0162 [0x92] Karanka-Tonka (ID: 17752348/0x010EE11C)->Render.Flags3 ^= 0x01
 13: 0x0168 [0x92] Cotta-Lotta (ID: 17752350/0x010EE11E)->Render.Flags3 ^= 0x01
 14: 0x016E [0x92] Tacca-Picca (ID: 17752351/0x010EE11F)->Render.Flags3 ^= 0x01
 15: 0x0174 [0x94] Tihk Rhumyie (ID: 17752346/0x010EE11A)->Render.Flags3 ^= 0x01
 16: 0x017A [0x94] Kuppo-Pippo (ID: 17752347/0x010EE11B)->Render.Flags3 ^= 0x01
 17: 0x0180 [0x94] Karanka-Tonka (ID: 17752348/0x010EE11C)->Render.Flags3 ^= 0x01
 18: 0x0186 [0x94] Cotta-Lotta (ID: 17752350/0x010EE11E)->Render.Flags3 ^= 0x01
 19: 0x018C [0x94] Tacca-Picca (ID: 17752351/0x010EE11F)->Render.Flags3 ^= 0x01
 20: 0x0192 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0193   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:          32 19 80 1F 00  1A 80 1B 80 03 80 1F 01     2............
01A0: 6F 4A 1A E1 0E 01 19 E1  0E 01 00                 oJ.........     
```

#### Opcodes

```
  0: 0x0193 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0196 [0x1F] MOVE_ENTITY: EventEntity moves to X=8.568*, Z=21.796*, Y=-1.000*
  2: 0x019E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01A0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01A1 [0x4A] Tihk Rhumyie (ID: 17752346/0x010EE11A) looks at Khoto Rokkorah (ID: 17752345/0x010EE119)
  5: 0x01AA [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01AB    |
| Data Size    | 121 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                   2F 00 20 E1 0E             /. ..
01B0: 01 2F 00 1F E1 0E 01 2F  00 1E E1 0E 01 2F 00 1D  ./...../...../..
01C0: E1 0E 01 2F 00 1B E1 0E  01 4E 00 20 E1 0E 01 4E  .../.....N. ...N
01D0: 00 1F E1 0E 01 4E 00 1E  E1 0E 01 4E 00 1D E1 0E  .....N.....N....
01E0: 01 4E 00 1B E1 0E 01 92  01 20 E1 0E 01 92 01 1F  .N....... ......
01F0: E1 0E 01 92 01 1E E1 0E  01 92 01 1D E1 0E 01 92  ................
0200: 01 1B E1 0E 01 94 01 20  E1 0E 01 94 01 1F E1 0E  ....... ........
0210: 01 94 01 1E E1 0E 01 94  01 1D E1 0E 01 94 01 1B  ................
0220: E1 0E 01 00                                       ....            
```

#### Opcodes

```
  0: 0x01AB [0x2F] Rahmi Yamilahto (ID: 17752352/0x010EE120)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x01B1 [0x2F] Tacca-Picca (ID: 17752351/0x010EE11F)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x01B7 [0x2F] Cotta-Lotta (ID: 17752350/0x010EE11E)->Render.Flags0 &= ~0x80000 // Bit 19
  3: 0x01BD [0x2F] Noh Ramyoh (ID: 17752349/0x010EE11D)->Render.Flags0 &= ~0x80000 // Bit 19
  4: 0x01C3 [0x2F] Kuppo-Pippo (ID: 17752347/0x010EE11B)->Render.Flags0 &= ~0x80000 // Bit 19
  5: 0x01C9 [0x4E] SET_ENTITY_HIDE_FLAG: Show Rahmi Yamilahto (ID: 17752352/0x010EE120)
  6: 0x01CF [0x4E] SET_ENTITY_HIDE_FLAG: Show Tacca-Picca (ID: 17752351/0x010EE11F)
  7: 0x01D5 [0x4E] SET_ENTITY_HIDE_FLAG: Show Cotta-Lotta (ID: 17752350/0x010EE11E)
  8: 0x01DB [0x4E] SET_ENTITY_HIDE_FLAG: Show Noh Ramyoh (ID: 17752349/0x010EE11D)
  9: 0x01E1 [0x4E] SET_ENTITY_HIDE_FLAG: Show Kuppo-Pippo (ID: 17752347/0x010EE11B)
 10: 0x01E7 [0x92] Rahmi Yamilahto (ID: 17752352/0x010EE120)->Render.Flags3 ^= 0x01
 11: 0x01ED [0x92] Tacca-Picca (ID: 17752351/0x010EE11F)->Render.Flags3 ^= 0x01
 12: 0x01F3 [0x92] Cotta-Lotta (ID: 17752350/0x010EE11E)->Render.Flags3 ^= 0x01
 13: 0x01F9 [0x92] Noh Ramyoh (ID: 17752349/0x010EE11D)->Render.Flags3 ^= 0x01
 14: 0x01FF [0x92] Kuppo-Pippo (ID: 17752347/0x010EE11B)->Render.Flags3 ^= 0x01
 15: 0x0205 [0x94] Rahmi Yamilahto (ID: 17752352/0x010EE120)->Render.Flags3 ^= 0x01
 16: 0x020B [0x94] Tacca-Picca (ID: 17752351/0x010EE11F)->Render.Flags3 ^= 0x01
 17: 0x0211 [0x94] Cotta-Lotta (ID: 17752350/0x010EE11E)->Render.Flags3 ^= 0x01
 18: 0x0217 [0x94] Noh Ramyoh (ID: 17752349/0x010EE11D)->Render.Flags3 ^= 0x01
 19: 0x021D [0x94] Kuppo-Pippo (ID: 17752347/0x010EE11B)->Render.Flags3 ^= 0x01
 20: 0x0223 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0224   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:             32 1C 80 1F  00 05 80 06 80 03 80 1F      2...........
0230: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0224 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0227 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.687*, Z=26.894*, Y=-1.000*
  2: 0x022F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0231 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0232   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:       4A 1A E1 0E 01 1C  E1 0E 01 6F 76 1A E1 0E    J........ov...
0240: 01 2B 1A E1 0E 01 1D 80  23 00                    .+......#.      
```

#### Opcodes

```
  0: 0x0232 [0x4A] Tihk Rhumyie (ID: 17752346/0x010EE11A) looks at Karanka-Tonka (ID: 17752348/0x010EE11C)
  1: 0x023B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x023C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Tihk Rhumyie (ID: 17752346/0x010EE11A) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0241 [0x2B] Tihk Rhumyie (ID: 17752346/0x010EE11A) [15099*]:
    → "Wait, wait. What happens next?"
  4: 0x0248 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0249 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024A   |
| Data Size    | 73 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                6C 1A E1 0E 01 1E            l.....
0250: 80 1F 80 6C 1B E1 0E 01  1E 80 1F 80 6C 1C E1 0E  ...l........l...
0260: 01 1E 80 1F 80 6C 1E E1  0E 01 1E 80 1F 80 6C 1F  .....l........l.
0270: E1 0E 01 1E 80 1F 80 4A  F0 FF FF 7F 19 E1 0E 01  .......J........
0280: 4A 19 E1 0E 01 F0 FF FF  7F 6F 76 19 E1 0E 01 1C  J........ov.....
0290: 20 80 00                                           ..             
```

#### Opcodes

```
  0: 0x024A [0x6C] FADE_ENTITY_COLOR(entity_id=Tihk Rhumyie (ID: 17752346/0x010EE11A), end_alpha=0*, fade_time=1*)
  1: 0x0253 [0x6C] FADE_ENTITY_COLOR(entity_id=Kuppo-Pippo (ID: 17752347/0x010EE11B), end_alpha=0*, fade_time=1*)
  2: 0x025C [0x6C] FADE_ENTITY_COLOR(entity_id=Karanka-Tonka (ID: 17752348/0x010EE11C), end_alpha=0*, fade_time=1*)
  3: 0x0265 [0x6C] FADE_ENTITY_COLOR(entity_id=Cotta-Lotta (ID: 17752350/0x010EE11E), end_alpha=0*, fade_time=1*)
  4: 0x026E [0x6C] FADE_ENTITY_COLOR(entity_id=Tacca-Picca (ID: 17752351/0x010EE11F), end_alpha=0*, fade_time=1*)
  5: 0x0277 [0x4A] LocalPlayer looks at Khoto Rokkorah (ID: 17752345/0x010EE119)
  6: 0x0280 [0x4A] Khoto Rokkorah (ID: 17752345/0x010EE119) looks at LocalPlayer
  7: 0x0289 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x028A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Khoto Rokkorah (ID: 17752345/0x010EE119) Render.Flags0 and Render.Flags3 conditions are met
  9: 0x028F [0x1C] WAIT(120* ticks)
 10: 0x0292 [0x00] END_REQSTACK()
```

### Event 991

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0293  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:          00                                          .            
```

#### Opcodes

```
  0: 0x0293 [0x00] END_REQSTACK()
```
