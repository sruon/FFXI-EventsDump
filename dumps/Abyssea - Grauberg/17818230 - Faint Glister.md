# 17818230 - Faint Glister

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 52 bytes                     |
| Total Events     | 2                            |
| References Count | 1                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [216](#event-216)     | 0x0001       |     21 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F3E      |        7998 |

## String References

- **7998**: There appears to be something on the ground.

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

### Event 216

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 48 00 80 23 29 05  F0 FF FF 7F 02 29 05 F0   BH..#)......)..
0010: FF FF 7F 03 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x48] [System] [7998*]:
    → "There appears to be something on the ground."
  2: 0x0005 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0006 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=LocalPlayer, tag_num=0x02)
  4: 0x000D [0x29] REQ_SET_WAIT(priority=0x05, entity_id=LocalPlayer, tag_num=0x03)
  5: 0x0014 [0x21] END_EVENT
  6: 0x0015 [0x00] END_REQSTACK()
```
