# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 104 bytes         |
| Total Events     | 6                 |
| References Count | 8                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [101](#event-101)        | 0x0002       |     13 |              3 |
| [65535.1](#event-655351) | 0x000F       |      6 |              2 |
| [65535.2](#event-655352) | 0x0015       |      1 |              1 |
| [65535.3](#event-655353) | 0x0016       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1B4FB     |      111867 |
|       1 | 0xE2CA      |       58058 |
|       2 | 0xFFFFF830  |  4294965296 |
|       3 | 0x0800      |        2048 |
|       4 | 0x009A      |         154 |
|       5 | 0xFFFFF98B  |  4294965643 |
|       6 | 0x0000      |           0 |
|       7 | 0x0B83      |        2947 |

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

### Event 65534

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

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       47 00 00 80 01 80  02 80 03 80 47 01 00       G.........G.. 
```

#### Opcodes

```
  0: 0x0002 [0x47] UPDATE_PLAYER_POS(111.867*, 58.058*, -2.000*, yaw=180.0°*)
  1: 0x000C [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               03                 .
0010: 02 10 0B 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x000F [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                00                                      .          
```

#### Opcodes

```
  0: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   37 04  80 05 80 06 80 07 80 00        7.........
```

#### Opcodes

```
  0: 0x0016 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.154*, z=-1.653*, y=0.000*, direction=259.0°*
  1: 0x001F [0x00] END_REQSTACK()
```
