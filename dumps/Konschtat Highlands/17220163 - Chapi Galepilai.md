# 17220163 - Chapi Galepilai

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Konschtat Highlands (ID: 108) |
| Block Size       | 128 bytes                     |
| Total Events     | 4                             |
| References Count | 8                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [912](#event-912)        | 0x0007       |      1 |              1 |
| [65535.1](#event-655351) | 0x0008       |     29 |              6 |
| [65535.2](#event-655352) | 0x0025       |     24 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1A98E     |      108942 |
|       1 | 0x3C509     |      247049 |
|       2 | 0x5E1A      |       24090 |
|       3 | 0x02C1      |         705 |
|       4 | 0x0050      |          80 |
|       5 | 0x1C43A     |      115770 |
|       6 | 0x3954C     |      234828 |
|       7 | 0x5DF9      |       24057 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 912

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      00                                  .        
```

#### Opcodes

```
  0: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          22 00 37 00 80 01 80 02          ".7.....
0010: 80 03 80 7E 01 F8 FF FF  7F 7E 02 F8 FF FF 7F 80  ...~.....~......
0020: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0008 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=108.942*, z=247.049*, y=24.090*, direction=62.0°*
  2: 0x0013 [0x7E] CHOCOBO_MOUNT: Mount chocobo on EventEntity (status = 5)
  3: 0x0019 [0x7E] CHOCOBO_MOUNT: Execute attachment function on EventEntity
  4: 0x001F [0x80] LOAD_WAIT(entity=EventEntity)
  5: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 04 80  79 00 F8 FF FF 7F 3F C2       2..y.....?.
0030: 06 01 1F 00 05 80 06 80  07 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0028 [0x79] EventEntity looks at Cid (ID: 17220159/0x0106C23F) (Basic look)
  2: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=115.770*, Z=234.828*, Y=24.057*
  3: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x003C [0x00] END_REQSTACK()
```
