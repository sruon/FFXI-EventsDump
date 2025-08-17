# 17179472 - Cousseraux

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 156 bytes                         |
| Total Events     | 6                                 |
| References Count | 6                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [9](#event-9)            | 0x0001       |      7 |              2 |
| [10](#event-10)          | 0x0008       |      7 |              2 |
| [115](#event-115)        | 0x000F       |     27 |              3 |
| [116](#event-116)        | 0x002A       |     27 |              3 |
| [65535.1](#event-655351) | 0x0045       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x000E      |          14 |
|       2 | 0x00A4      |         164 |
|       3 | 0x00D9      |         217 |
|       4 | 0x0000      |           0 |
|       5 | 0x0172      |         370 |

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

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               92                 .
0010: 01 F8 FF FF 7F B6 0B 00  80 01 80 02 80 03 80 03  ................
0020: 80 03 80 03 80 04 80 04  80 00                    ..........      
```

#### Opcodes

```
  0: 0x000F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0015 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=14*, head=164*, body=217*, hands=217*, legs=217*, feet=217*, main=0*, sub=0*)
  2: 0x0029 [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                92 01 F8 FF FF 7F            ......
0030: B6 0B 00 80 01 80 02 80  03 80 03 80 03 80 03 80  ................
0040: 04 80 04 80 00                                    .....           
```

#### Opcodes

```
  0: 0x002A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0030 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=14*, head=164*, body=217*, hands=217*, legs=217*, feet=217*, main=0*, sub=0*)
  2: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                B6 0B 00  80 01 80 02 80 03 80 03       ...........
0050: 80 03 80 03 80 05 80 04  80 00                    ..........      
```

#### Opcodes

```
  0: 0x0045 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=14*, head=164*, body=217*, hands=217*, legs=217*, feet=217*, main=370*, sub=0*)
  1: 0x0059 [0x00] END_REQSTACK()
```
