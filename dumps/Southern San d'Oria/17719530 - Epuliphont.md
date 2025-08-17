# 17719530 - Epuliphont

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 88 bytes                      |
| Total Events     | 5                             |
| References Count | 5                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [734](#event-734)        | 0x0002       |      1 |              1 |
| [65535.2](#event-655352) | 0x0003       |     10 |              2 |
| [65535.3](#event-655353) | 0x000D       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x9072      |       36978 |
|       1 | 0xFFFFF2B7  |  4294963895 |
|       2 | 0xFFFFF449  |  4294964297 |
|       3 | 0x0643      |        1603 |
|       4 | 0x005A      |          90 |

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

### Event 734

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.978*, z=-3.401*, y=-2.999*, direction=140.9°*
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         1C 04 80               ...
0010: 4A EA 60 0E 01 E9 60 0E  01 6F 76 EA 60 0E 01 00  J.`...`..ov.`...
```

#### Opcodes

```
  0: 0x000D [0x1C] WAIT(90* ticks)
  1: 0x0010 [0x4A] Epuliphont (ID: 17719530/0x010E60EA) looks at Leservieus (ID: 17719529/0x010E60E9)
  2: 0x0019 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x001A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Epuliphont (ID: 17719530/0x010E60EA) Render.Flags0 and Render.Flags3 conditions are met
  4: 0x001F [0x00] END_REQSTACK()
```
