# 17780990 - Rolandienne

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 464 bytes             |
| Total Events     | 10                    |
| References Count | 19                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [20041](#event-20041)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     39 |              9 |
| [20047](#event-20047)    | 0x0029       |      1 |              1 |
| [65535.2](#event-655352) | 0x002A       |     24 |              6 |
| [65535.3](#event-655353) | 0x0042       |     61 |             11 |
| [65535.4](#event-655354) | 0x007F       |     52 |             12 |
| [65535.5](#event-655355) | 0x00B3       |    115 |             25 |
| [65535.6](#event-655356) | 0x0126       |     13 |              3 |
| [65535.7](#event-655357) | 0x0133       |     22 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0008      |           8 |
|       1 | 0x006E      |         110 |
|       2 | 0x000D      |          13 |
|       3 | 0xFFFF586D  |  4294924397 |
|       4 | 0xFFFF39BA  |  4294916538 |
|       5 | 0x0000      |           0 |
|       6 | 0xFFFF5DD0  |  4294925776 |
|       7 | 0xFFFF4106  |  4294918406 |
|       8 | 0x000A      |          10 |
|       9 | 0xFFFF580A  |  4294924298 |
|      10 | 0xFFFF3D62  |  4294917474 |
|      11 | 0x000B      |          11 |
|      12 | 0x0024      |          36 |
|      13 | 0x0007      |           7 |
|      14 | 0x000F      |          15 |
|      15 | 0x001E      |          30 |
|      16 | 0x0004      |           4 |
|      17 | 0x001A      |          26 |
|      18 | 0x0001      |           1 |

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

### Event 20041

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
| Data Size    | 39 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       6E FE 50 0F 01 00  80 99 FE 50 0F 01 1C 01    n.P......P....
0010: 80 32 02 80 1F 00 03 80  04 80 05 80 1F 01 1F 00  .2..............
0020: 06 80 07 80 05 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0002 [0x6E] Rolandienne (ID: 17780990/0x010F50FE) uses emote 8*
  1: 0x0009 [0x99] Wait for Rolandienne (ID: 17780990/0x010F50FE) animation to complete
  2: 0x000E [0x1C] WAIT(110* ticks)
  3: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  4: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.899*, Z=-50.758*, Y=0.000*
  5: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=-41.520*, Z=-48.890*, Y=0.000*
  7: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0028 [0x00] END_REQSTACK()
```

### Event 20047

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 08 80 1F 00 09            2.....
0030: 80 0A 80 05 80 1F 01 6F  4A F8 FF FF 7F F6 50 0F  .......oJ.....P.
0040: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.998*, Z=-49.822*, Y=0.000*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0038 [0x4A] EventEntity looks at Nantoto (ID: 17780982/0x010F50F6)
  5: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 61 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       6E FF 50 0F 01 0B  80 99 FF 50 0F 01 6E 00    n.P......P..n.
0050: 51 0F 01 0C 80 99 00 51  0F 01 6E FD 50 0F 01 0B  Q......Q..n.P...
0060: 80 99 FD 50 0F 01 6E FE  50 0F 01 0D 80 99 FE 50  ...P..n.P......P
0070: 0F 01 6E F0 FF FF 7F 0C  80 99 F0 FF FF 7F 00     ..n............ 
```

#### Opcodes

```
  0: 0x0042 [0x6E] Fhelm Jobeizat (ID: 17780991/0x010F50FF) uses emote 11*
  1: 0x0049 [0x99] Wait for Fhelm Jobeizat (ID: 17780991/0x010F50FF) animation to complete
  2: 0x004E [0x6E] Isakoth (ID: 17780992/0x010F5100) uses emote 36*
  3: 0x0055 [0x99] Wait for Isakoth (ID: 17780992/0x010F5100) animation to complete
  4: 0x005A [0x6E] Eternal Flame (ID: 17780989/0x010F50FD) uses emote 11*
  5: 0x0061 [0x99] Wait for Eternal Flame (ID: 17780989/0x010F50FD) animation to complete
  6: 0x0066 [0x6E] Rolandienne (ID: 17780990/0x010F50FE) uses emote 7*
  7: 0x006D [0x99] Wait for Rolandienne (ID: 17780990/0x010F50FE) animation to complete
  8: 0x0072 [0x6E] LocalPlayer uses emote 36*
  9: 0x0079 [0x99] Wait for LocalPlayer animation to complete
 10: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               4A                 J
0080: FE 50 0F 01 FF 50 0F 01  1C 08 80 4A F6 50 0F 01  .P...P.....J.P..
0090: FF 50 0F 01 1C 0E 80 4A  FF 50 0F 01 F6 50 0F 01  .P.....J.P...P..
00A0: 6F 76 FE 50 0F 01 6F 76  F6 50 0F 01 6F 76 FF 50  ov.P..ov.P..ov.P
00B0: 0F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x007F [0x4A] Rolandienne (ID: 17780990/0x010F50FE) looks at Fhelm Jobeizat (ID: 17780991/0x010F50FF)
  1: 0x0088 [0x1C] WAIT(10* ticks)
  2: 0x008B [0x4A] Nantoto (ID: 17780982/0x010F50F6) looks at Fhelm Jobeizat (ID: 17780991/0x010F50FF)
  3: 0x0094 [0x1C] WAIT(15* ticks)
  4: 0x0097 [0x4A] Fhelm Jobeizat (ID: 17780991/0x010F50FF) looks at Nantoto (ID: 17780982/0x010F50F6)
  5: 0x00A0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00A1 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rolandienne (ID: 17780990/0x010F50FE) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x00A6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00A7 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Nantoto (ID: 17780982/0x010F50F6) Render.Flags0 and Render.Flags3 conditions are met
  9: 0x00AC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x00AD [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Fhelm Jobeizat (ID: 17780991/0x010F50FF) Render.Flags0 and Render.Flags3 conditions are met
 11: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00B3    |
| Data Size    | 115 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          4A FF 50 0F 01  00 51 0F 01 1C 08 80 4A     J.P...Q.....J
00C0: FE 50 0F 01 00 51 0F 01  1C 0E 80 4A F6 50 0F 01  .P...Q.....J.P..
00D0: 00 51 0F 01 1C 08 80 6F  76 FF 50 0F 01 6F 76 FE  .Q.....ov.P..ov.
00E0: 50 0F 01 6F 76 F6 50 0F  01 1C 0F 80 6E FD 50 0F  P..ov.P.....n.P.
00F0: 01 10 80 99 FD 50 0F 01  6E F6 50 0F 01 10 80 99  .....P..n.P.....
0100: F6 50 0F 01 1C 0F 80 6E  FE 50 0F 01 0B 80 99 FE  .P.....n.P......
0110: 50 0F 01 1C 08 80 6E FF  50 0F 01 11 80 99 FF 50  P.....n.P......P
0120: 0F 01 1C 0F 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00B3 [0x4A] Fhelm Jobeizat (ID: 17780991/0x010F50FF) looks at Isakoth (ID: 17780992/0x010F5100)
  1: 0x00BC [0x1C] WAIT(10* ticks)
  2: 0x00BF [0x4A] Rolandienne (ID: 17780990/0x010F50FE) looks at Isakoth (ID: 17780992/0x010F5100)
  3: 0x00C8 [0x1C] WAIT(15* ticks)
  4: 0x00CB [0x4A] Nantoto (ID: 17780982/0x010F50F6) looks at Isakoth (ID: 17780992/0x010F5100)
  5: 0x00D4 [0x1C] WAIT(10* ticks)
  6: 0x00D7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00D8 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Fhelm Jobeizat (ID: 17780991/0x010F50FF) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x00DD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x00DE [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rolandienne (ID: 17780990/0x010F50FE) Render.Flags0 and Render.Flags3 conditions are met
 10: 0x00E3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x00E4 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Nantoto (ID: 17780982/0x010F50F6) Render.Flags0 and Render.Flags3 conditions are met
 12: 0x00E9 [0x1C] WAIT(30* ticks)
 13: 0x00EC [0x6E] Eternal Flame (ID: 17780989/0x010F50FD) uses emote 4*
 14: 0x00F3 [0x99] Wait for Eternal Flame (ID: 17780989/0x010F50FD) animation to complete
 15: 0x00F8 [0x6E] Nantoto (ID: 17780982/0x010F50F6) uses emote 4*
 16: 0x00FF [0x99] Wait for Nantoto (ID: 17780982/0x010F50F6) animation to complete
 17: 0x0104 [0x1C] WAIT(30* ticks)
 18: 0x0107 [0x6E] Rolandienne (ID: 17780990/0x010F50FE) uses emote 11*
 19: 0x010E [0x99] Wait for Rolandienne (ID: 17780990/0x010F50FE) animation to complete
 20: 0x0113 [0x1C] WAIT(10* ticks)
 21: 0x0116 [0x6E] Fhelm Jobeizat (ID: 17780991/0x010F50FF) uses emote 26*
 22: 0x011D [0x99] Wait for Fhelm Jobeizat (ID: 17780991/0x010F50FF) animation to complete
 23: 0x0122 [0x1C] WAIT(30* ticks)
 24: 0x0125 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0126   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                   1C 08  80 4A F8 FF FF 7F F0 FF        ...J......
0130: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0126 [0x1C] WAIT(10* ticks)
  1: 0x0129 [0x4A] EventEntity looks at LocalPlayer
  2: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 22 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          2A 08 F0 FF FF  7F 1C 08 80 6E F8 FF FF     *........n...
0140: 7F 12 80 99 F8 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x0133 [0x2A] GET_REQ_LEVEL(level=8, entity_id=LocalPlayer)
  1: 0x0139 [0x1C] WAIT(10* ticks)
  2: 0x013C [0x6E] EventEntity uses emote 1*
  3: 0x0143 [0x99] Wait for EventEntity animation to complete
  4: 0x0148 [0x00] END_REQSTACK()
```
