# 17339237 - Elivira Gogol

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 408 bytes               |
| Total Events     | 14                      |
| References Count | 25                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0044       |     42 |              9 |
| [65535.9](#event-655359)   | 0x006E       |     13 |              3 |
| [65535.10](#event-6553510) | 0x007B       |     75 |             14 |
| [65535.11](#event-6553511) | 0x00C6       |     30 |              7 |
| [19](#event-19)            | 0x00E4       |      1 |              1 |
| [20](#event-20)            | 0x00E5       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x003C      |          60 |
|       4 | 0x000D      |          13 |
|       5 | 0x269AD     |      158125 |
|       6 | 0xFFFF8D72  |  4294937970 |
|       7 | 0xFFFFC2CC  |  4294951628 |
|       8 | 0x2726E     |      160366 |
|       9 | 0xFFFF8EB2  |  4294938290 |
|      10 | 0xFFFFC2F8  |  4294951672 |
|      11 | 0x0102      |         258 |
|      12 | 0x268F4     |      157940 |
|      13 | 0xFFFF8E95  |  4294938261 |
|      14 | 0xFFFFC2DB  |  4294951643 |
|      15 | 0x26140     |      155968 |
|      16 | 0xFFFF91D5  |  4294939093 |
|      17 | 0xFFFFC2F1  |  4294951665 |
|      18 | 0x0013      |          19 |
|      19 | 0x260C1     |      155841 |
|      20 | 0xFFFFA229  |  4294943273 |
|      21 | 0xFFFFC472  |  4294952050 |
|      22 | 0x25676     |      153206 |
|      23 | 0xFFFFAFED  |  4294946797 |
|      24 | 0xFFFFC299  |  4294951577 |

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

### Event 65535.1

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 42 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             4A F8 FF FF  7F 56 93 08 01 1C 03 80      J....V......
0050: 59 04 F8 FF FF 7F 04 80  1F 00 05 80 06 80 07 80  Y...............
0060: 1F 01 1F 00 08 80 09 80  0A 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x0044 [0x4A] EventEntity looks at Lilisette (ID: 17339222/0x01089356)
  1: 0x004D [0x1C] WAIT(60* ticks)
  2: 0x0050 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  3: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=158.125*, Z=-29.326*, Y=-15.668*
  4: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0062 [0x1F] MOVE_ENTITY: EventEntity moves to X=160.366*, Z=-29.006*, Y=-15.624*
  6: 0x006A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x006C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            6E F8                n.
0070: FF FF 7F 0B 80 99 F8 FF  FF 7F 00                 ...........     
```

#### Opcodes

```
  0: 0x006E [0x6E] EventEntity uses emote 258*
  1: 0x0075 [0x99] Wait for EventEntity animation to complete
  2: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 75 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   7B F8 FF FF 7F             {....
0080: 59 04 F8 FF FF 7F 04 80  1F 00 08 80 09 80 0A 80  Y...............
0090: 1F 01 1F 00 0C 80 0D 80  0E 80 1F 01 1F 00 0F 80  ................
00A0: 10 80 11 80 1F 01 6F 4A  F8 FF FF 7F 35 93 08 01  ......oJ....5...
00B0: 6F 76 F8 FF FF 7F 66 12  80 65 93 08 01 65 93 08  ov....f..e...e..
00C0: 01 74 6C 6B 30 00                                 .tlk0.          
```

#### Opcodes

```
  0: 0x007B [0x7B] EventEntity stops talking
  1: 0x0080 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  2: 0x0088 [0x1F] MOVE_ENTITY: EventEntity moves to X=160.366*, Z=-29.006*, Y=-15.624*
  3: 0x0090 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0092 [0x1F] MOVE_ENTITY: EventEntity moves to X=157.940*, Z=-29.035*, Y=-15.653*
  5: 0x009A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x009C [0x1F] MOVE_ENTITY: EventEntity moves to X=155.968*, Z=-28.203*, Y=-15.631*
  7: 0x00A4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x00A6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x00A7 [0x4A] EventEntity looks at ex07 (ID: 17339189/0x01089335)
 10: 0x00B0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x00B1 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 12: 0x00B6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Elivira Gogol (ID: 17339237/0x01089365), Elivira Gogol (ID: 17339237/0x01089365)], work=19*
 13: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 30 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   59 04  F8 FF FF 7F 04 80 1F 00        Y.........
00D0: 13 80 14 80 15 80 1F 01  1F 00 16 80 17 80 18 80  ................
00E0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x00C6 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x00CE [0x1F] MOVE_ENTITY: EventEntity moves to X=155.841*, Z=-24.023*, Y=-15.246*
  2: 0x00D6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D8 [0x1F] MOVE_ENTITY: EventEntity moves to X=153.206*, Z=-20.499*, Y=-15.719*
  4: 0x00E0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00E2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00E3 [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             00                                        .           
```

#### Opcodes

```
  0: 0x00E4 [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E5  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x00E5 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00EB [0x00] END_REQSTACK()
```
