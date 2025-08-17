# 17133937 - test guest

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 72 bytes                    |
| Total Events     | 2                           |
| References Count | 1                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [600](#event-600)     | 0x0001       |     41 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2AAE      |       10926 |

## String References

- **10926**: Freelance ID: $0, Area of Attack: $1, Contract Status: [No affiliation/San d'Oria/Bastok/Windurst/Beastman 1/Beastman 2/Beastman 3/Beastman 4], San d'Orian Reputation: $3, Bastokan Reputation: $4, Windurstian Reputation: $5

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

### Event 600

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 03 00 00 02  10 03 01 00 03 10 03 02    .B............
0010: 00 04 10 03 03 00 05 10  03 04 00 06 10 03 05 00  ................
0020: 07 10 1D 00 80 23 20 00  21 00                    .....# .!.      
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x0009 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  4: 0x000E [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  5: 0x0013 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  6: 0x0018 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[6]
  7: 0x001D [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[7]
  8: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=10926*)
    → "Freelance ID: $0, Area of Attack: $1, Contract Status: [No affiliation/San d'Oria/Bastok/Windurst/Beastman 1/Beastman 2/Beastman 3/Beastman 4], San d'Orian Reputation: $3, Bastokan Reputation: $4, Windurstian Reputation: $5"
  9: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0026 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0028 [0x21] END_EVENT
 12: 0x0029 [0x00] END_REQSTACK()
```
