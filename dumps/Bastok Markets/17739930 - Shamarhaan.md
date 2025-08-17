# 17739930 - Shamarhaan

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Bastok Markets (ID: 235) |
| Block Size       | 112 bytes                |
| Total Events     | 5                        |
| References Count | 9                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [439](#event-439)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     11 |              3 |
| [65535.2](#event-655352) | 0x000D       |     14 |              4 |
| [65535.3](#event-655353) | 0x001B       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE41B1  |  4294853041 |
|       1 | 0xFFFFE8A9  |  4294961321 |
|       2 | 0x0000      |           0 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFE28EF  |  4294846703 |
|       5 | 0xFFFFDB6C  |  4294957932 |
|       6 | 0x0042      |          66 |
|       7 | 0xFFFE2984  |  4294846852 |
|       8 | 0xFFFFD44B  |  4294956107 |

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

### Event 439

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
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1F 00 00 80 01 80  02 80 1F 01 00             ...........   
```

#### Opcodes

```
  0: 0x0002 [0x1F] MOVE_ENTITY: EventEntity moves to X=-114.255*, Z=-5.975*, Y=0.000*
  1: 0x000A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         32 03 80               2..
0010: 1F 00 04 80 05 80 06 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x000D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-120.593*, Z=-9.364*, Y=0.066*
  2: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1F 00 07 80 08             .....
0020: 80 02 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=-120.444*, Z=-11.189*, Y=0.000*
  1: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0025 [0x00] END_REQSTACK()
```
