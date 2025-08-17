# 16883762 - Parelbriaux

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 128 bytes                   |
| Total Events     | 5                           |
| References Count | 8                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [113](#event-113)        | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     10 |              2 |
| [65535.2](#event-655352) | 0x0018       |     24 |              5 |
| [65535.3](#event-655353) | 0x0030       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1977      |        6519 |
|       1 | 0x5EC5      |       24261 |
|       2 | 0xFFFFA76D  |  4294944621 |
|       3 | 0x09AF      |        2479 |
|       4 | 0x000D      |          13 |
|       5 | 0x1001      |        4097 |
|       6 | 0x6430      |       25648 |
|       7 | 0xFFFFA6EC  |  4294944492 |

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

### Event 113

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 00         .............  
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            37 00                7.
0010: 80 01 80 02 80 03 80 00                           ........        
```

#### Opcodes

```
  0: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=6.519*, z=24.261*, y=-22.675*, direction=217.9°*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          79 00 F8 FF FF 7F 28 A0          y.....(.
0020: 01 01 32 04 80 1F 00 05  80 06 80 07 80 1F 01 00  ..2.............
```

#### Opcodes

```
  0: 0x0018 [0x79] EventEntity looks at Prishe (ID: 16883752/0x0101A028) (Basic look)
  1: 0x0022 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=4.097*, Z=25.648*, Y=-22.804*
  3: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 37 00 80 01 80 02 80 03  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0030 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=6.519*, z=24.261*, y=-22.675*, direction=217.9°*
  1: 0x0039 [0x00] END_REQSTACK()
```
