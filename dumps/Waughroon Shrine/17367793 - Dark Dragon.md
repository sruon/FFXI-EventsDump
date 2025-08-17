# 17367793 - Dark Dragon

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Waughroon Shrine (ID: 144) |
| Block Size       | 128 bytes                  |
| Total Events     | 4                          |
| References Count | 9                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |     24 |              5 |
| [32001](#event-32001)    | 0x0019       |     16 |              3 |
| [65535.1](#event-655351) | 0x0029       |     19 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0xFFFD52DC  |  4294791900 |
|       3 | 0xFFFDE50E  |  4294829326 |
|       4 | 0xEB9D      |       60317 |
|       5 | 0x069A      |        1690 |
|       6 | 0x001E      |          30 |
|       7 | 0x007F      |         127 |
|       8 | 0x010E      |         270 |

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

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 92 01 F8 FF FF 7F 6C   "./...........l
0010: F8 FF FF 7F 00 80 01 80  00                       .........       
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             2F 00 F8 FF FF 7F 37           /.....7
0020: 02 80 03 80 04 80 05 80  00                       .........       
```

#### Opcodes

```
  0: 0x0019 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-175.396*, z=-137.970*, y=60.317*, direction=148.5°*
  2: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1C 06 80 92 00 F8 FF           .......
0030: FF 7F 6C F8 FF FF 7F 07  80 08 80 00              ..l.........    
```

#### Opcodes

```
  0: 0x0029 [0x1C] WAIT(30* ticks)
  1: 0x002C [0x92] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  2: 0x0032 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=127*, fade_time=270*)
  3: 0x003B [0x00] END_REQSTACK()
```
