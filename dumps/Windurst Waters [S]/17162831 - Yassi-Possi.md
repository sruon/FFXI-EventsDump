# 17162831 - Yassi-Possi

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 112 bytes                    |
| Total Events     | 4                            |
| References Count | 4                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [191](#event-191)     | 0x0001       |     20 |              3 |
| [192](#event-192)     | 0x0015       |     20 |              3 |
| [197](#event-197)     | 0x0029       |     20 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x25988     |      153992 |
|       1 | 0xFFFFB701  |  4294948609 |
|       2 | 0x03E7      |         999 |
|       3 | 0x017F      |         383 |

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

### Event 191

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 4F E2 05 01 BA  4F E2 05 01 00 80 01 80   ..O....O.......
0010: 02 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0001 [0x92] Yassi-Possi (ID: 17162831/0x0105E24F)->Render.Flags3 ^= 0x01
  1: 0x0007 [0xBA] SET_ENTITY_POSITION(entity_id=Yassi-Possi (ID: 17162831/0x0105E24F), pos_x=153.992*, pos_z=-18.687*, pos_y=0.999*, direction=33.7°*)
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 192

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                92 01 4F  E2 05 01 BA 4F E2 05 01       ..O....O...
0020: 00 80 01 80 02 80 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x0015 [0x92] Yassi-Possi (ID: 17162831/0x0105E24F)->Render.Flags3 ^= 0x01
  1: 0x001B [0xBA] SET_ENTITY_POSITION(entity_id=Yassi-Possi (ID: 17162831/0x0105E24F), pos_x=153.992*, pos_z=-18.687*, pos_y=0.999*, direction=33.7°*)
  2: 0x0028 [0x00] END_REQSTACK()
```

### Event 197

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             92 01 4F E2 05 01 BA           ..O....
0030: 4F E2 05 01 00 80 01 80  02 80 03 80 00           O............   
```

#### Opcodes

```
  0: 0x0029 [0x92] Yassi-Possi (ID: 17162831/0x0105E24F)->Render.Flags3 ^= 0x01
  1: 0x002F [0xBA] SET_ENTITY_POSITION(entity_id=Yassi-Possi (ID: 17162831/0x0105E24F), pos_x=153.992*, pos_z=-18.687*, pos_y=0.999*, direction=33.7°*)
  2: 0x003C [0x00] END_REQSTACK()
```
