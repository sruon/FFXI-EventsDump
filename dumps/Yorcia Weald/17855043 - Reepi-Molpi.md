# 17855043 - Reepi-Molpi

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 196 bytes              |
| Total Events     | 9                      |
| References Count | 17                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [109](#event-109)        | 0x0001       |      1 |              1 |
| [111](#event-111)        | 0x0002       |      1 |              1 |
| [114](#event-114)        | 0x0003       |     21 |              2 |
| [65535.1](#event-655351) | 0x0018       |     14 |              4 |
| [65535.2](#event-655352) | 0x0026       |     14 |              4 |
| [65535.3](#event-655353) | 0x0034       |     21 |              2 |
| [118](#event-118)        | 0x0049       |      1 |              1 |
| [120](#event-120)        | 0x004A       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0004      |           4 |
|       1 | 0x0001      |           1 |
|       2 | 0x0014      |          20 |
|       3 | 0x008F      |         143 |
|       4 | 0x0017      |          23 |
|       5 | 0x0000      |           0 |
|       6 | 0x000D      |          13 |
|       7 | 0x3E524     |      255268 |
|       8 | 0x61A00     |      399872 |
|       9 | 0x011F      |         287 |
|      10 | 0x3F0F6     |      258294 |
|      11 | 0x63F85     |      409477 |
|      12 | 0x05FC      |        1532 |
|      13 | 0x0005      |           5 |
|      14 | 0x0006      |           6 |
|      15 | 0x0158      |         344 |
|      16 | 0x0039      |          57 |

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

### Event 109

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

### Event 111

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

### Event 114

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          B6 0B 00 80 01  80 02 80 03 80 04 80 03     .............
0010: 80 03 80 05 80 05 80 00                           ........        
```

#### Opcodes

```
  0: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=1*, head=20*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          32 06 80 1F 00 07 80 08          2.......
0020: 80 09 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=255.268*, Z=399.872*, Y=0.287*
  2: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   32 06  80 1F 00 0A 80 0B 80 0C        2.........
0030: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0026 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0029 [0x1F] MOVE_ENTITY: EventEntity moves to X=258.294*, Z=409.477*, Y=1.532*
  2: 0x0031 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             B6 0B 0D 80  0E 80 05 80 0F 80 05 80      ............
0040: 0F 80 10 80 05 80 05 80  00                       .........       
```

#### Opcodes

```
  0: 0x0034 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=6*, head=0*, body=344*, hands=0*, legs=344*, feet=57*, main=0*, sub=0*)
  1: 0x0048 [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0049  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             00                             .      
```

#### Opcodes

```
  0: 0x0049 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                00                           .     
```

#### Opcodes

```
  0: 0x004A [0x00] END_REQSTACK()
```
