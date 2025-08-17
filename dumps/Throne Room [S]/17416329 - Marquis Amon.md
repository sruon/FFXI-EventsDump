# 17416329 - Marquis Amon

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Throne Room [S] (ID: 156) |
| Block Size       | 140 bytes                 |
| Total Events     | 8                         |
| References Count | 6                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32004](#event-32004)    | 0x0001       |     11 |              3 |
| [65535.1](#event-655351) | 0x000C       |      5 |              2 |
| [65535.2](#event-655352) | 0x0011       |     10 |              2 |
| [65535.3](#event-655353) | 0x001B       |     10 |              2 |
| [65535.4](#event-655354) | 0x0025       |     10 |              2 |
| [65535.5](#event-655355) | 0x002F       |     10 |              2 |
| [32001](#event-32001)    | 0x0039       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x033E      |         830 |
|       1 | 0x08AD      |        2221 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0078      |         120 |
|       5 | 0x0080      |         128 |

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

### Event 32004

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F B6  00 00 80 00               ...........    
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=830*)
  2: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      B6 00 01 80              ....
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x000C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2221*)
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    6C 89 C0 09 01 02 80  03 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0011 [0x6C] FADE_ENTITY_COLOR(entity_id=Marquis Amon (ID: 17416329/0x0109C089), end_alpha=0*, fade_time=1*)
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   6C 89 C0 09 01             l....
0020: 02 80 04 80 00                                    .....           
```

#### Opcodes

```
  0: 0x001B [0x6C] FADE_ENTITY_COLOR(entity_id=Marquis Amon (ID: 17416329/0x0109C089), end_alpha=0*, fade_time=120*)
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                6C 89 C0  09 01 05 80 04 80 00          l......... 
```

#### Opcodes

```
  0: 0x0025 [0x6C] FADE_ENTITY_COLOR(entity_id=Marquis Amon (ID: 17416329/0x0109C089), end_alpha=128*, fade_time=120*)
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               6C                 l
0030: 89 C0 09 01 05 80 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x002F [0x6C] FADE_ENTITY_COLOR(entity_id=Marquis Amon (ID: 17416329/0x0109C089), end_alpha=128*, fade_time=1*)
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0039  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             92 01 F8 FF FF 7F A5           .......
0040: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0039 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003F [0xA5] EventEntity->Flags3.BallistaTeam |= 0x08  // Set bit 3 of BallistaTeam
  2: 0x0041 [0x00] END_REQSTACK()
```
