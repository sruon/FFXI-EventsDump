# 17167266 - Kayeel-Payeel

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 280 bytes                      |
| Total Events     | 15                             |
| References Count | 15                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [105](#event-105)          | 0x0001       |      1 |              1 |
| [110](#event-110)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     21 |              2 |
| [65535.2](#event-655352)   | 0x0018       |     21 |              2 |
| [107](#event-107)          | 0x002D       |      1 |              1 |
| [112](#event-112)          | 0x002E       |      1 |              1 |
| [65535.3](#event-655353)   | 0x002F       |     28 |              7 |
| [65535.4](#event-655354)   | 0x004B       |      1 |              1 |
| [65535.5](#event-655355)   | 0x004C       |     18 |              4 |
| [65535.6](#event-655356)   | 0x005E       |     10 |              2 |
| [65535.7](#event-655357)   | 0x0068       |      9 |              3 |
| [65535.8](#event-655358)   | 0x0071       |      9 |              3 |
| [65535.9](#event-655359)   | 0x007A       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0084       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0006      |           6 |
|       1 | 0x0004      |           4 |
|       2 | 0x0000      |           0 |
|       3 | 0x0068      |         104 |
|       4 | 0x0005      |           5 |
|       5 | 0x0009      |           9 |
|       6 | 0x00DC      |         220 |
|       7 | 0x0156      |         342 |
|       8 | 0x001E      |          30 |
|       9 | 0x0028      |          40 |
|      10 | 0x296A4     |      169636 |
|      11 | 0xFFFFDA72  |  4294957682 |
|      12 | 0xFFFFF311  |  4294963985 |
|      13 | 0x0001      |           1 |
|      14 | 0x0080      |         128 |

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

### Event 105

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

### Event 110

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
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          B6 0B 00 80 01  80 02 80 03 80 03 80 03     .............
0010: 80 03 80 02 80 02 80 00                           ........        
```

#### Opcodes

```
  0: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=4*, head=0*, body=104*, hands=104*, legs=104*, feet=104*, main=0*, sub=0*)
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          B6 0B 04 80 05 80 06 80          ........
0020: 06 80 06 80 06 80 06 80  07 80 02 80 00           .............   
```

#### Opcodes

```
  0: 0x0018 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=9*, head=220*, body=220*, hands=220*, legs=220*, feet=220*, main=342*, sub=0*)
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         00                     .  
```

#### Opcodes

```
  0: 0x002D [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 28 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               79                 y
0030: 00 F8 FF FF 7F A1 F3 05  01 1C 08 80 32 09 80 1F  ............2...
0040: 00 0A 80 0B 80 0C 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x002F [0x79] EventEntity looks at Zolku-Azolku (ID: 17167265/0x0105F3A1) (Basic look)
  1: 0x0039 [0x1C] WAIT(30* ticks)
  2: 0x003C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=169.636*, Z=-9.614*, Y=-3.311*
  4: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   00                         .    
```

#### Opcodes

```
  0: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      22 00 2F 00              "./.
0050: F8 FF FF 7F 6C F8 FF FF  7F 02 80 0D 80 00        ....l.........  
```

#### Opcodes

```
  0: 0x004C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x004E [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0054 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            6C F8                l.
0060: FF FF 7F 0E 80 0D 80 00                           ........        
```

#### Opcodes

```
  0: 0x005E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0068  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          22 00 2F 00 F8 FF FF 7F          "./.....
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0068 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x006A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0071  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    22 01 2F 01 F8 FF FF  7F 00                     "./......      
```

#### Opcodes

```
  0: 0x0071 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0073 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                6C F8 FF FF 7F 02            l.....
0080: 80 0D 80 00                                       ....            
```

#### Opcodes

```
  0: 0x007A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             6C F8 FF FF  7F 0E 80 0D 80 00            l.........  
```

#### Opcodes

```
  0: 0x0084 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x008D [0x00] END_REQSTACK()
```
