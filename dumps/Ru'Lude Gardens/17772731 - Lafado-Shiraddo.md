# 17772731 - Lafado-Shiraddo

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 140 bytes                 |
| Total Events     | 5                         |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10070](#event-10070)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     27 |              5 |
| [65535.2](#event-655352) | 0x001D       |     15 |              3 |
| [65535.3](#event-655353) | 0x002C       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0324      |         804 |
|       1 | 0x4882      |       18562 |
|       2 | 0x0BB7      |        2999 |
|       3 | 0x0CD5      |        3285 |
|       4 | 0xB967      |       47463 |
|       5 | 0xFFFF0340  |  4294902592 |
|       6 | 0x270F      |        9999 |
|       7 | 0x03F6      |        1014 |
|       8 | 0x000D      |          13 |
|       9 | 0x06A8      |        1704 |
|      10 | 0x20A8      |        8360 |

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

### Event 10070

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
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       2F 00 BB 30 0F 01  4E 00 BB 30 0F 01 37 00    /..0..N..0..7.
0010: 80 01 80 02 80 03 80 80  BB 30 0F 01 00           .........0...   
```

#### Opcodes

```
  0: 0x0002 [0x2F] Lafado-Shiraddo (ID: 17772731/0x010F30BB)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0008 [0x4E] SET_ENTITY_HIDE_FLAG: Show Lafado-Shiraddo (ID: 17772731/0x010F30BB)
  2: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.804*, z=18.562*, y=2.999*, direction=288.7°*
  3: 0x0017 [0x80] LOAD_WAIT(entity=Lafado-Shiraddo (ID: 17772731/0x010F30BB))
  4: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         37 04 80               7..
0020: 05 80 06 80 07 80 80 BB  30 0F 01 00              ........0...    
```

#### Opcodes

```
  0: 0x001D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=47.463*, z=-64.704*, y=9.999*, direction=89.1°*
  1: 0x0026 [0x80] LOAD_WAIT(entity=Lafado-Shiraddo (ID: 17772731/0x010F30BB))
  2: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      32 08 80 1F              2...
0030: 00 09 80 0A 80 02 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x002C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=1.704*, Z=8.360*, Y=2.999*
  2: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0039 [0x00] END_REQSTACK()
```
